#include <stdio.h>
#include <stdlib.h>

char buf[400];

int main() {
  setvbuf(stdout,NULL,2,0);
  setvbuf(stdin,NULL,2,0);
  puts("Welcome to Format Fun!");
  puts("I'll print one, AND ONLY ONE, string for you.");
  puts("Enter your string below:");
  fgets(buf, 400, stdin);
  printf(buf);
}

int win() {
  system("cat flag.txt");
}
