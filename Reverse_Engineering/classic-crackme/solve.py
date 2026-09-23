target = "xjagpediegzqlnaudqfwyncpvkqneusycourkguerjpzcbstcc"
input_len = len(target)


def transform_char(char_val, i_1):
    uVar1 = (i_1 % 255 >> 1 & 0x55) + (i_1 % 255 & 0x55)
    uVar1 = ((uVar1 >> 2) & 0x33) + (uVar1 & 0x33)
    
    # Apply the shift logic from the loop
    # iVar2 = ((uVar1 >> 4) + val - 0x61 + (uVar1 & 0xf))
    # result = (iVar2 % 26) + ord('a')
    
    shift = ((uVar1 >> 4) + (uVar1 & 0xf)) % 26
    return shift

# We need to reverse the shift 3 times
shifts = []
for i_1 in range(input_len):
    s = transform_char(0, i_1)
    shifts.append(s)

password = ""
for i_1 in range(input_len):
    
    val = ord(target[i_1]) - ord('a')
    
    
    total_shift = (shifts[i_1] * 3) % 26
    original_val = (val - total_shift) % 26
    password += chr(original_val + ord('a'))

print(f"The password: {password}")
