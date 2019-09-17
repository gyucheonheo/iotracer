#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *
generate_rand_string (length)
     size_t length;
{
  static char charset[] = "abcdefghijklmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.-#'?!";
  char *rand_str;
  rand_str = malloc(length+1);
  size_t i;
  if ( rand_str ){
    for(i = 0; i < length; i++){
      int key = rand() % (int)(sizeof(charset) - 1);
      rand_str[i] = charset[key];
    }
    rand_str[length] = '\0';
  }
  return rand_str;
}
