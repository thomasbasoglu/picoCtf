def asm4(input_string):
    # Step 1: Calculate the string length (mimicking the first assembly loop)
    # For "picoCTF_574ff", this will be 13
    str_len = len(input_string)
    
    # Step 2: Initialize local variables
    # [ebp-0x10] starts at 0x240
    local_10 = 0x240  
    # [ebp-0x8] starts at 1 (the loop counter)
    local_8 = 1       
    
    # Converting the string into a list of ASCII integer values to match assembly behavior
    string_bytes = [ord(char) for char in input_string]
    
    # Step 3: The Second Loop (mimicking <+55> to <+151>)
    # The assembly loop runs while local_8 < (str_len - 1)
    while local_8 < (str_len - 1):
        
        # Line <+55> to <+66>: Grab character at current index
        current_char = string_bytes[local_8]
        
        # Line <+69> to <+83>: Grab character right BEFORE current index
        prev_char = string_bytes[local_8 - 1]
        
        # Line <+86> to <+95>: Subtract them and add to the running total
        diff1 = current_char - prev_char
        ebx = local_10 + diff1
        
        # Line <+98> to <+112>: Grab character right AFTER current index
        next_char = string_bytes[local_8 + 1]
        
        # Line <+115> to <+129>: Grab current character again
        # Line <+131> to <+135>: Subtract them, add to EBX, and update total
        diff2 = next_char - current_char
        local_10 = ebx + diff2
        
        # Line <+138>: Increment loop counter
        local_8 += 1
        
    # Line <+153>: Return the final total (EAX)
    return local_10

# Run the function WALLAAAA
result = asm4("picoCTF_574ff")

# Print the result formatted as a hex string
print(f"Flag: {hex(result)}")