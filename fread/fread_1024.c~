#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#define SZ 1024

int main(){
	FILE *fp = fopen("test1024.txt", "w+");
	char *buf = (char *)malloc(sizeof(char)*SZ);
	fwrite(buf, SZ, 1, fp);
	sleep(10);
	fread(buf, SZ, 1, fp);
	fclose(fp);
}




