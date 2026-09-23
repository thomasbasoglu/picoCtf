# The target string that the buffer must equal
target = "jU5t_a_sna_3lpm1cg04e_u_4_m6rb42"

# Create an empty list of 32 characters to hold our reconstructed password
password = [""] * 32

# Replicate Loop 1: i from 0 to 7
for i in range(0, 8):
    password[i] = target[i]

# Replicate Loop 2: i from 8 to 15
for i in range(8, 16):
    password[23 - i] = target[i]

# Replicate Loop 3: i from 16 to 31, skipping by 2 (even indices)
for i in range(16, 32, 2):
    password[46 - i] = target[i]

# Replicate Loop 4: i from 31 down to 17, skipping by 2 (odd indices)
for i in range(31, 16, -2):
    password[i] = target[i]

# Join the list into the final string
flag_payload = "".join(password)
print(f"Payload: {flag_payload}")
print(f"Full Flag: picoCTF{{{flag_payload}}}")