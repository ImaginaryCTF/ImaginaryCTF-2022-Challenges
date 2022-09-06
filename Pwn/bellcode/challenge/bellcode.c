#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>

int main() {
  setvbuf(stdout,NULL,2,0);
  setvbuf(stdin,NULL,2,0);

  mmap((unsigned char*) 0xfac300, 0x2000, 7, MAP_SHARED | MAP_ANONYMOUS, -1, 0);

  puts("What's your shellcode?");
  fgets((unsigned char*) 0xfac300, 0x1000, stdin);

  for (unsigned char *i= (unsigned char*)0xfac300; i<(unsigned char*)(0xfad300); i++) {
    if ((*i) % 5 != 0) {
      puts("Seems that you tried to escape. Try harder™.");
      exit(-1);
    }
  }

  puts("OK. Running your shellcode now!");
  int (*sc)() = (int(*)()) 0xfac300;
  sc();
}
