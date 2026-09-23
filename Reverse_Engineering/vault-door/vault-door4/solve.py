my_bytes = [
    106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
    0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
    0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o61 , 0o63 ,
    ord('d') , ord('f') , ord('6') , ord('1') , ord('8') , ord('a') , ord('2') , ord('3')
]

payload = ''.join(chr(b) for b in my_bytes)
print(f'picoCTF{{{payload}}}')