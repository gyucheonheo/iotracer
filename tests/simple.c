#include <stdio.h>
#include <unistd.h>

int main(){
  sleep(10);
  fopen("test.txt", "w");
}
