import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(cipher):
    enc = ""
    for i in range(0, len(cipher), 2):
        binary = "{0:04b}".format(ALPHABET.index(cipher[i])) + "{0:04b}".format(ALPHABET.index(cipher[i+1]))
        enc += chr(int(binary, 2))
    return enc

def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]

encflag = "fegdeogdgecoeocgcgchcfcffccfca"

for key in ALPHABET:
    dec = ""
    for c in encflag:
        # Calculate the inverse key to turn addition into subtraction
        k_val = ord(key) - LOWERCASE_OFFSET
        inverse_k_val = (16 - k_val) % 16
        inverse_key_char = ALPHABET[inverse_k_val]
        
        # Call the original shift function exactly like the video loop
        dec += shift(c, inverse_key_char)
        
    try:
        b16 = b16_decode(dec)
        print(key, b16)
    except Exception:
        continue
