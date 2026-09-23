import base64

encoded_string = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"
decoded_string = base64.b64decode(encoded_string).decode('utf-8')
print(f"picoCTF{{{decoded_string}}}")