#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#define SZ 512

int main(){
  FILE *fd = fopen("test512.txt", "w+");
  char *buf = (char *)malloc(sizeof(char)*SZ);

  fwrite(buf,SZ, 1, fd);
  sleep(atoi(argv[1]));
  fread(buf, SZ, 1, fd);
  fclose(fd);
}
