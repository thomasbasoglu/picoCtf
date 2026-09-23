#!/usr/bin/env python3
from pwn import *
import struct
import time

# Target info 
HOST = 'mysterious-sea.picoctf.net'
PORT = 60678

def extract_secret(raw_bytes):
    """
    Scans the raw binary blob for the x86 machine code pattern:
    mov dword ptr [rbp - offset], IMM  ->  \xc7\x45
    """
    pattern = b'\xc7\x45'
    idx = raw_bytes.find(pattern)
    
    if idx == -1:
        return None
        
    # Layout: [c7 45] [offset] [4-byte immediate value]
    # Skip the 2-byte opcode and 1-byte stack offset to read the raw data bytes
    value_start = idx + 3
    value_bytes = raw_bytes[value_start:value_start+4]
    
    # Unpack the 4 little-endian bytes into a standard unsigned integer
    secret_int = struct.unpack('<I', value_bytes)[0]
    return secret_int

def main():
    log.info(f"Establishing network connection to {HOST}:{PORT}")
    
    try:
        p = remote(HOST, PORT)
    except Exception as e:
        log.failure(f"Could not connect: {e}")
        return

    # Loop through all 20 required verification rounds
    for round_num in range(1, 21):
        log.info(f"--- Processing Round {round_num}/20 ---")
        
        try:
            # grab the incoming raw hex stream
            p.recvuntil(b"bytes:\n")
            hex_string = p.recvline().strip().decode()
            
            # Convert text hex to bytes
            binary_blob = bytes.fromhex(hex_string)
            
            # Rip the secret key out of the opcodes
            secret = extract_secret(binary_blob)
            if secret is None:
                log.failure("Failed to isolate the opcode signature in this block!")
                p.close()
                return
                
            log.success(f"Extracted Secret: {secret} (Hex: {hex(secret)})")
            
            # Wait for the prompt (matching loosely without a strict trailing newline)
            p.recvuntil(b"secret?") 
            
            # Brief stabilization pause before sending data
            time.sleep(0.05)
            
            # Ship the payload back to the remote server
            p.sendline(str(secret).encode())
            
            # Print the Correct
            feedback = p.recvline().strip().decode()
            log.info(f"Server response: {feedback}")
            
        except Exception as e:
            log.failure(f"An error occurred during round {round_num}: {e}")
            break
            
    # After successfully matching 20 times, intercept the flag payload
    log.success("All rounds processed! Catching flag payload:")
    try:
        remaining_output = p.recvall(timeout=5).decode(errors='ignore')
        print(remaining_output)
    except Exception as e:
        log.failure(f"Failed to read final response: {e}")

if __name__ == '__main__':
    main()