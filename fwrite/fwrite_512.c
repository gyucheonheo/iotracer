#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#define SZ 512

int main(int argc, char** argv){
  FILE *fd = fopen("test.txt", "w");
  char *buf = (char *)malloc(sizeof(char)*SZ);
  sleep(atoi(argv[1]));
  fwrite(buf,SZ, 1, fd);
  fclose(fd);
}
