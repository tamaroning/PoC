#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char buffer[32];

void vuln(){
    char local[32];

    printf("buffer : 0x%x\n", &buffer);

    fgets(local, 128, stdin);
    strcpy(buffer, local);
    
    return;
}

void func(){
    system("/bin/ls");
}

int main(){
    vuln();

    return 0;
}