from cryptography.fernet import Fernet

with open('key', 'rb') as f:
    key = f.read().strip()


with open('webhook', 'rb') as f:
    ciphertext = f.read().strip()

f = Fernet(key)
try:
    print(f.decrypt(ciphertext).decode())
except Exception as e:
    print("Decryption failed. Check your file names and contents!")
    print("Error details:", e)
