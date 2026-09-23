import ast
import socket

# Connect to remote host 
host = "verbal-sleep.picoctf.net"
port = 65251
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


# Using a list to collect chunks of data 
chunks = []
while True:
    chunk = client.recv(4096)
    if not chunk:
        break

    chunks.append(chunk)

#Combine chunks and convert to string 
data = b"".join(chunks).decode("utf-8")

encoded_data = ast.literal_eval(data.strip())


def unscramble(cypher: list[list[str] | str]):
    """Unscramble the list using the picoCTF logic."""
    encoded = []
    for obj_list in cypher:
        for obj in obj_list:
            if not isinstance(obj, list):
                encoded.append(obj)


    return encoded

def reverse_flag(encoded: list[str]) -> str:
    return "".join(chr(int(c, 16)) for c in encoded)

decoded_hex = unscramble(encoded_data)
flag = reverse_flag(decoded_hex)
print(flag)