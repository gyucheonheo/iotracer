#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
int main(int argc, char** argv){
  sleep(atoi(argv[1]));
  FILE *fd = fopen("test.txt", "w+");
  fclose(fd);
}
