/*
Gray Hat Python
CH 8 Example
page 115

Format String Demonstration

Passing a format specifier to print() with no
actual input.  printf() assumes the next value on
the stack is the number to be formatted and prints
0x4bcbf058 (for test = '%x')
*/

#include <stdio.h>

int main(){

  char* test = "%s";
  printf(test);

  return 0;
}
