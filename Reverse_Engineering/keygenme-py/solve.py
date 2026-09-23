import hashlib

username = b"BENNETT"
static_part_1 = "picoCTF{1n_7h3_kk3y_of_"
static_part_2 = "}"

# Calculate the SHA-256 hash of the username
user_hash = hashlib.sha256(username).hexdigest()

# Reconstruct the dynamic 8-character part based on the code's logic
dynamic_part = (
    user_hash[4] +
    user_hash[5] +
    user_hash[3] +
    user_hash[6] +
    user_hash[2] +
    user_hash[7] +
    user_hash[1] +
    user_hash[8]
)


flag = static_part_1 + dynamic_part + static_part_2
print(f"Your flag/license key is: {flag}")
