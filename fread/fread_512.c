#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#define SZ 512

int main(){
  FILE *fd = fopen("test512.txt", "w+");
  char *buf = (char *)malloc(sizeof(char)*SZ);

  fwrite(buf,SZ, 1, fd);
  sleep(10);
  fread(buf, SZ, 1, fd);
  fclose(fd);
}
