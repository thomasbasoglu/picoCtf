import struct

# The target integers from the Java checkPassword method
target_ints = [
    1096770097,
    1952395366,
    1600270708,
    1601398833,
    1716808014,
    1734305378,
    825374004,
    912340068
]

# Reconstructing 32 character strings 
pass_bytes = b""
for num in target_ints:
    # unpacks or packs a 32 bit unsigned interger in Big endian format
    pass_bytes+= struct.pack(">I", num)

# Converting byte array into a string 
flag_in = pass_bytes.decode('utf-8')
flag = f"picoCTF{{{flag_in}}}"

print(flag)