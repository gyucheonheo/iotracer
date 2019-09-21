#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#define SZ 1024

int main(int argc, char**argv){
	FILE *fp = fopen("test1024.txt", "w+");
	char *buf = (char *)malloc(sizeof(char)*SZ);
	fwrite(buf, SZ, 1, fp);
	sleep(argv[1]));
	fread(buf, SZ, 1, fp);
	fclose(fp);
}




