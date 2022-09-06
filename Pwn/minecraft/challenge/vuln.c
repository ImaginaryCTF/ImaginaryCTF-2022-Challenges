#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <string.h>

char *mem[16];
long sizes[16];
int kept=0;
int replaced=0;

int main() {
  system("clear");
  setvbuf(stdout,NULL,2,0);
  setvbuf(stdin,NULL,2,0);
  char c;
  int index;
  puts("It's Minecraft time! Your speedrun starts... now!");
  while (1) {
    puts("(p)lace a block");
    puts("(b)reak a block");
    puts("(r)eplace a block");
    puts("(l)eak the end poem");
    scanf("%c%*c", &c);
    if (c=='p') {
      puts("idx: ");
      scanf("%d%*c", &index);
      if ((index < 0) || (index > 16)) {_Exit(0);}
      puts("len: ");
      scanf("%ld%*c", &sizes[index]);
      if (sizes[index] < 0x500 || sizes[index] > 0x10000) { _Exit(0); }
      mem[index] = (char*) malloc(sizes[index]);
      puts("type of block: ");
      if ((index < 0) || (index > 16)) {_Exit(0);}
      read(0, mem[index], sizes[index]);
    }
    else if (c=='b') {
      puts("idx: ");
      scanf("%d%*c", &index);
      if ((index < 0) || (index > 16)) {_Exit(0);}
      free(mem[index]);
      puts("keep in inventory? ");
      scanf("%c%*c", &c);
      if (c == 'y' && kept == 0) {
        kept++;
      }
      else {
        puts("Inventory full!");
        mem[index] = NULL;
      }
    }
    else if (c=='r') {
      puts("Careful... you can replace a block once.");
      if (replaced) {_Exit(0);}
      replaced++;
      puts("idx: ");
      scanf("%d%*c", &index);
      if ((index < 0) || (index > 16)) {_Exit(0);}
      puts("type of block: ");
      read(0, mem[index], sizes[index]);
    }
    else if (c=='l') {
      puts("Careful... you can only leak the end poem once.");
      puts("idx: ");
      scanf("%d%*c", &index);
      if ((index < 0) || (index > 16)) {_Exit(0);}
      if (strchr(mem[index], 'n') != 0) {_Exit(0);}
      if (strlen(mem[index]) > 9) {_Exit(0);}
      printf(mem[index]);
      _Exit(0);
    }
  }
}
