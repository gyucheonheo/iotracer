#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include "randstr.h"
int main(){
	for(;;){
	  FILE *fd = fopen("test.txt", "w+");
	  char *buf = malloc(sizeof(char)*8);
	  buf = generate_rand_string(8);
	  char *buf1 = malloc(sizeof(char)*8);
	  fwrite(buf, 8, 1, fd);
	  sleep(5);
	  fread(buf1, 8, 1, fd);
	  fclose(fd);
	}

}
