from pwn import *

expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTM0JTMyJTYzJTM2JTM0JTMwJTM5JTYy"
base64_dec = b64d(expected).decode('utf-8')
payload = urldecode(base64_dec)
flag = f"picoCTF{{{payload}}}"

print(flag)

