from pwn import *
import re 

HOST = "crystal-peak.picoctf.net"
PORT = 59251

r = remote(HOST,PORT)

# Read the math challenge line 
challenge = r.recvuntil(b"? ").decode().strip()
log.info(f"Recieved Challenge: '{challenge}'")

# Regex to pull numbers and operator 
match = re.search(r"What is (\d+)\s+([\+\-\*])\s+(\d+)", challenge)

if not match:
    log.error("Failed to calc math q")
    exit(1)

num1, op, num2 = int(match.group(1)), match.group(2), int(match.group(3))

# Calculate multiplier

if op == '+': multiplier = num1 + num2
elif op == '-': multiplier = num1 - num2
elif op == '*': multiplier = num1 * num2

log.success(f"Calculated answer/multiplier: {multiplier}")

# Sending the answer
r.sendline(str(multiplier).encode())

# Skip the answer
r.recvuntil(b"Encoded flag values:\n")

# Read the array strings 
encoded_data = r.recvline().decode().strip()
log.info(f"Raw Encoded Array: {encoded_data}")

# Convert comma string array into a list of integers
encoded_integers = [int(x.strip()) for x in encoded_data.split(",") if x.strip()]

# 4. Decode the flag: Divide each integer by the multiplier, convert to ASCII char
flag_chars = [chr(num // multiplier) for num in encoded_integers]
real_flag = "".join(flag_chars)

print("\n" + "="*40)
log.success(f"REAL DECRYPTED FLAG: {real_flag}")
print("="*40)

r.close()