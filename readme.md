This repositry has vulerable C programs and exploit code for them written in Python.   
  
bof1.c : it has a BOF bug.  
bof2.c : it has a BOF bug.  
  
retaddr.py(bof1) : overwrite return address with function address  
shellcode.py(bof1) : overwrite return address with address on which shellcode is put and run shellcode  
ret2plt.py(bof2) : overwrite return address with system@plt and execute /bin/sh  
  


----- my memo from here -----

retaddr.py require no SSP, no PIE  
shellcode.py no NX, no ASLR in addition to these  
  
gcc -m32 -fno-stack-protector -no-pie -z execstack -o bof1 bof1.c  
gcc -m32 -fno-stack-protector -no-pie -o bof2 bof2.c  
  
python -c "print('A'*44+'\x2c\x06\x00\x00')"  
  
  
gcc compile options  

32bit ELF : -m32  
disable SSP : -fno-stack-protector  
able SSP : -fstack-protector  
disable NX bit :-z execstack  
disable PIE :-no-pie  
  
Disable ASLR :  
sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'  
able ASLR :  
sudo bash -c 'echo 2 > /proc/sys/kernel/randomize_va_space'  
  
python -c "print('A'*44+'\x2c\x06\x00\x00')"  

