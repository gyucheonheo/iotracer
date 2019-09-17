#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#define SZ 512

int main(){
  FILE *fd = fopen("test.txt", "w");
  char *buf = (char *)malloc(sizeof(char)*SZ);
  sleep(10);
  fwrite(buf,SZ, 1, fd);
  fclose(fd);
}
