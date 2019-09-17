#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#define SZ 65536

int main(){
  FILE *fd = fopen("test65536.txt", "w+");
  char *buf = malloc(sizeof(char)*SZ);
  fwrite(buf, SZ, 1, fd);
  sleep(10);
  fread(buf, SZ, 1, fd);
  fclose(fd);
}

  // 8, 128, 2048, 128kb, 512kb, 1mb, 2mb
