encrypted_data = [
    4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0, 57, 32, 108, 23, 48, 4, 
    9, 70, 7, 110, 36, 8, 108, 7, 49, 10, 4, 86, 43, 104, 44, 91, 7, 
    18, 106, 124, 89, 78
]

key_base = "t_Jo3"

# Try all cyclic shifts of the key
for shift in range(len(key_base)):
    # Rotate the key
    current_key = key_base[shift:] + key_base[:shift]
    
    # Attempt decryption
    decoded = ""
    for i in range(len(encrypted_data)):
        decoded += chr(encrypted_data[i] ^ ord(current_key[i % len(current_key)]))
    
    # Check if it looks like a flag
    if "picoCTF" in decoded:
        print(f"Found it with key rotation '{current_key}':")
        print(decoded)
        break