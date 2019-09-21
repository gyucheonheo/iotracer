#include <stdio.h>
#include <unistd.h>

int main(){
  sleep(2);
  FILE *fd = fopen("test.txt", "a+");
  fclose(fd);
}
