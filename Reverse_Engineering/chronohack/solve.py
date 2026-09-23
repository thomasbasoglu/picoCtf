from pwn import *
import random
import time

def get_random(length, seed_time):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(seed_time)
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s

# --- CONFIGURATION ---
HOST = 'verbal-sleep.picoctf.net'
PORT = 52644

TOKEN_LENGTH = 20
base_offset = -50  # Start slightly in the past to catch a fast server clock

print(f" Firing up Chronohack solver against {HOST}:{PORT}")
print(" Sweeping sequential millisecond frames...")
print("-" * 60)

while True:
    try:
        # Establish a single connection
        io = remote(HOST, PORT, level='error')
        
        # Grab the baseline reference time right when connecting
        # This will be our initial guess for the remote seed
        start_seed = int(time.time() * 1000) + base_offset
        
        print(f" Connected. Testing 50ms window starting at seed: {start_seed} (Offset: {base_offset}ms)")
        
        # Use the server's 50-guess allowance to sweep a continuous block of seeds
        for guess_num in range(50):
            # Read up to the input prompt
            io.recvuntil(b'Enter your guess for the token (or exit):')
            
            # The server updates its internal state linearly inside the loop. 
            # We match it by incrementing our candidate seed by 1ms per iteration.
            current_seed = start_seed + guess_num
            payload = get_random(TOKEN_LENGTH, current_seed)
            
            # Send our calculated token guess
            io.sendline(payload.encode())
            
            # Read the server's response
            response = io.recvline()
            
            # If the response doesn't say 'Sorry', we broke through to the flag!
            if b'Sorry' not in response and b'Incorrect' not in response:
                print(f"\n" + "="*50)
                print(f" SUCCESS!!!!! Found the matching seed: {current_seed}")
                print(f" Server Output: {response.decode().strip()}")
                print(f"SWITCHING INTERACTIVE")
                print("="*50)
                io.interactive()
                exit(0)
        
        # If all 50 guesses in this session missed, close the socket safely
        io.close()
        
        # Advance the baseline window forward by 40ms for the next connection 
        # (leaving a 10ms overlap to protect against network jitter)
        base_offset += 40
        
    except Exception as e:
        print(f" Connection dropped or errored: {e}. Retrying same window...")
        time.sleep(1)