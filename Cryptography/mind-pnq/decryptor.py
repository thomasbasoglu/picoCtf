# Given values (Replace with your actual numbers)
c = 15341890103764929939105506004034128738090325640037083301857608662849501626260517 
n = 948406957756830799684818171639547165784816468744946013083947881743680617123566349
e = 65537

# Found from factoring n (Example primes)
p = 1891771437429478964908181306574287207137
q = 501332739776173570344039681219489434626477

# 0Calculate Phi and d
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

# Decrypt the ciphertext
# Decrypt the ciphertext
m = pow(c, d, n)

print("Decrypted Integer:", m)

try:
    # 1. Format to hex string, ensuring an even length by padding with a leading zero if needed
    hex_str = f"{m:x}"
    if len(hex_str) % 2 != 0:
        hex_str = "0" + hex_str
        
    # 2. Convert to raw bytes
    raw_bytes = bytes.fromhex(hex_str)
    
    # 3. Handle Endianness
    # Try big-endian first, then try little-endian (reversed) if a known pattern like 'pico' is found
    decoded_big = raw_bytes.decode('utf-8', errors='ignore')
    decoded_little = raw_bytes[::-1].decode('utf-8', errors='ignore')
    
    if "pico" in decoded_big or "pico" in decoded_big.lower():
        print("Decrypted Message:", decoded_big)
    elif "pico" in decoded_little or "pico" in decoded_little.lower():
        print("Decrypted Message (Reversed/Little-Endian):", decoded_little)
    else:
        # Fallback to printing both if neither explicitly matches the string 'pico'
        print("Decrypted Message (Big Endian):", decoded_big)
        print("Decrypted Message (Little Endian):", decoded_little)

except Exception as e:
    print(f"Could not decode to string. Error: {e}")
    print("Raw hex:", hex(m))
