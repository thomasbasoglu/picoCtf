from Crypto.Util.number import long_to_bytes, inverse

# These values should be in the 'values' or 'output' file provided by the challenge
# or shown when you connect via netcat
n = 19127886410951858559112046782540553759076137632782160407450484594735627725821045908856258042701835366131373177334940063168356378327485408564631504016845322 # Paste the long number for N here
e = 65537 # Paste e here (usually 65537)
c = 3692459420048046622831032932259980724187855725764531260792892166644393210034207111020685671883714498295323756444832646704831347301768302970028801291217121
 # Paste the ciphertext here

# The Attack
p = 2
q = n // 2

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)

print("Flag found:")
print(long_to_bytes(m).decode())
