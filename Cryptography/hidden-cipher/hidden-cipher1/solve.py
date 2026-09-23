from pwn import *

HOST = 'candy-mountain.picoctf.net'
PORT = 57136

log.info(f"Connecting to {HOST}:{PORT}...")
r = remote(HOST, PORT)

banner = r.recvline().decode().strip()
log.info(f"Server says: '{banner}'")

hex_ciphertext = r.recvline().decode().strip()
log.success(f"Received Ciphertext: {hex_ciphertext}")

key = b"S3Cr3t"
ciphertext_bytes = bytes.fromhex(hex_ciphertext)

plaintext = bytearray()
for i in range(len(ciphertext_bytes)):
	plaintext.append(ciphertext_bytes[i] ^ key[i % len(key)])

print("\n" + "="*40)
log.success(f"REAL FLAG: {plaintext.decode(errors='ignore')}")
print("="*40)

r.close()
