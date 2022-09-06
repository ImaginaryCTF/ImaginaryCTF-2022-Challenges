#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  char buf[256];
  char choice;
  char scratch[256];
  puts("Can you get the flag?");
  fgets(buf, 50, stdin);
  mprotect(buf, 100, 7);
  printf("are you sure though ");
  scanf("%c%*c", &choice);
  printf("are you really sure ");
  scanf("%s%*c", scratch);
  printf("%d %f %i\n", atol(scratch), atof(scratch), atoi(scratch));
  printf("really? ");
  chdir("/");
  if (strcmp(buf, "jctf{n0t_the_real_flag?_or_is_it?}\n") == 0) {
    puts("correct");
    exit(0);
  }
  else {
    puts("wrong!");
    exit(0);
  }
}
