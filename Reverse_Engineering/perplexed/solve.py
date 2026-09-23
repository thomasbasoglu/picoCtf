# The hidden byte sequence from the binary
secret = [
    -0x1f & 0xff, -0x59 & 0xff, 0x1e, -8 & 0xff, ord('u'), ord('#'), ord('{'), ord('a'),
    -0x47 & 0xff, -99 & 0xff, -4 & 0xff, ord('Z'), ord('['), -0x21 & 0xff, ord('i'), 0xd2,
    -2 & 0xff, 0x1b, -0x13 & 0xff, -0xc & 0xff, -0x13 & 0xff, ord('g'), -0xc & 0xff
]

# 1. Reconstruct the continuous bitstream (8 bits per secret byte)
bitstream = ""
for byte in secret:
    bitstream += f"{byte:08b}"

# 2. Slice the bitstream into 7-bit chunks instead of 8
chunks = [bitstream[i:i+7] for i in range(0, len(bitstream), 7)]

# 3. Convert each 7-bit block back to its actual ASCII character
flag = ""
for chunk in chunks:
    if len(chunk) == 7: # Drop any incomplete trailing bits
        flag += chr(int(chunk, 2))

print(flag)
