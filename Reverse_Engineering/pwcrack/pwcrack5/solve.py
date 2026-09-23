import hashlib

dictionary_file = 'dictionary.txt'
correct_pw_hash = open('level5.hash.bin', 'rb').read()

def hash_pw(pw_str):
     pw_bytes = bytearray()
     pw_bytes.extend(pw_str.encode())
     m = hashlib.md5()
     m.update(pw_bytes)
     return m.digest()

with open(dictionary_file, 'r', encoding='utf-8', errors='ignore') as f:
     found = False
     for line in f:
          # Cleaning up the line 
          pw = line.strip()

          # Skip empty lines
          if not pw:
               continue

          # hashcheck
          if hash_pw(pw) == correct_pw_hash:
               print(f"The correct pass is: {pw}")
               found = True
               break

     if not found:
          print("No match")

