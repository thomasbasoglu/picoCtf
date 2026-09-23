encoded_string ="灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽" 

flag = ""
for char in encoded_string:
    # Get the 16-bit integer value
    val = ord(char)
    
    # Get the high byte (shift back right 8)
    flag += chr(val >> 8)
    
    # Get the low byte (mask the high part)
    flag += chr(val & 0xFF)

print(flag)
