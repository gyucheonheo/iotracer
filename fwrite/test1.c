#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
int main(){
  for(;;){
    FILE *fd = fopen("asdf.txt", "w");
    char *buf = (char *)malloc(sizeof(char)*1);
    sleep(5);
    fwrite(buf, 1, 1, fd);
    fclose(fd);
  }
}
