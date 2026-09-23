import re

file_path = "values"  

with open(file_path, "r") as f:
    content = f.read()

try:
    # Captures 'N:', 'n:', 'N =', etc.
    n = int(re.search(r'n\s*(\([a-z]\))?\s*[:=]\s*(\d+)', content, re.IGNORECASE).group(2))
    
    # Captures 'e:', 'e =', etc.
    e = int(re.search(r'e\s*[:=]\s*(\d+)', content, re.IGNORECASE).group(1))
    
    # Captures 'c:', 'ciphertext:', 'ciphertext (c):', etc.
    c = int(re.search(r'(c|ciphertext)\s*(\([a-z]\))?\s*[:=]\s*(\d+)', content, re.IGNORECASE).group(3))

    print("[+] Parameters parsed successfully!")
    print(f"e = {e}")
    print(f"n bits = {n.bit_length()}")
    
except AttributeError as err:
    print("[-] Regex parsing failed. Double-check the formatting inside your 'values' file.")
    print("File Content Peek:\n", content[:200])
    raise err

def hrd_cube_root(val):
    low = 0
    high = val
    while low <= high:
        mid = (low + high) // 2
        mid_cubed = mid ** 3
        if mid_cubed == val:
            return mid
        elif mid_cubed < val:
            low = mid + 1
        else:
            high = mid - 1
    return high

print("[*] Brute-forcing k to find the padded flag...")

# Iterate through possible values of k
for k in range(0, 100000):  # Included 0 just in case it didn't actually wrap
    target = c + k * n
    m = hrd_cube_root(target)
    
    if m ** 3 == target:
        # Convert integer to raw bytes safely
        hex_str = f"{m:x}"
        if len(hex_str) % 2 != 0:
            hex_str = "0" + hex_str
        raw_bytes = bytes.fromhex(hex_str)
        
        # Decode and force string representation
        decoded_big = raw_bytes.decode('utf-8', errors='ignore')
        decoded_little = raw_bytes[::-1].decode('utf-8', errors='ignore')
        
        # Check if 'pico' is anywhere inside the string
        if "pico" in decoded_big.lower():
            print(f"\n[+] Success! Found matching root at k = {k}")
            print(f"[!] Full Decrypted String (Big Endian):\n{decoded_big}")
            break
        elif "pico" in decoded_little.lower():
            print(f"\n[+] Success! Found matching root at k = {k} (Reversed)")
            print(f"[!] Full Decrypted String (Little Endian):\n{decoded_little}")
            break
else:
    print("[-] Failed to find a cube root containing 'pico'. Try raising the range of k.")