#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(){
  for(;;){
char *buf = "Hello World\n";
  FILE *fd = fopen("hello1.txt", "w");
  fwrite(buf, sizeof("Hello World\n"), 1, fd);
  sleep(3);
  fclose(fd);
  }
  return 0;
}
