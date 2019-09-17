#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
  for(;;){
    sleep(8);
    FILE *fd = fopen("test.txt", "r");
    char *buf = (char *)malloc(sizeof(char)*1);
    fread(buf, 1, 1, fd);
    fclose(fd);
  }
}
