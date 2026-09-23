from scapy.all import rdpcap

def extract_and_decrypt_pcap(pcap_filename, output_filename, key=42):
    print(f"[*] Reading {pcap_filename}...")
    packets = rdpcap(pcap_filename)
    
    # 1. Stitch together the continuous raw payloads from the single TCP stream
    raw_payload = b""
    for packet in packets:
        if packet.haslayer('Raw'):
            raw_payload += packet['Raw'].load
            
    print(f"[+] Total raw encrypted payload extracted: {len(raw_payload)} bytes")
    
    # 2. Reverse the math: (b - key) % 256
    print(f"[*] Decrypting stream using key offset: {key}...")
    decrypted_bytes = bytes([(b - key) % 256 for b in raw_payload])
    
    # 3. Double-check what kind of file we actually uncovered
    if decrypted_bytes.startswith(b"\xff\xd8\xff"):
        print("[+] Magic Bytes Verified: Valid JPEG Image discovered!")
    elif b"picoCTF" in decrypted_bytes:
        print("[+] Found standard flag string inside the stream text!")
    else:
        print("[!] Warning: Output doesn't start with standard JPEG headers. Trying brute-force search for correct file alignment...")
        # Check all possible keys just in case it wasn't 42
        for test_key in range(256):
            test_bytes = bytes([(b - test_key) % 256 for b in raw_payload])
            if test_bytes.startswith(b"\xff\xd8\xff") or b"picoCTF{" in test_bytes:
                print(f"[++] Found perfect match using key offset: {test_key}!")
                decrypted_bytes = test_bytes
                break

    # 4. Save the repaired data
    with open(output_filename, "wb") as f:
        f.write(decrypted_bytes)
    print(f"[+] Clean file saved to: {output_filename}")

if __name__ == "__main__":
    # Point directly to your pcap file shown in your 'ls' output
    extract_and_decrypt_pcap("packets.pcap", "recovered_flag.jpg", key=42)
