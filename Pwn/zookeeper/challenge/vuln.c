#include <seccomp.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <string.h>

struct management {
  int size;
  char *ptr;
  char metadata[64];
};

struct management *mem[16];

void __attribute__ ((constructor)) setup() {
  setvbuf(stdout,NULL,2,0);
  setvbuf(stdin,NULL,2,0);
  scmp_filter_ctx ctx;
  ctx = seccomp_init(SCMP_ACT_KILL);
  seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 0);
  seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);
  seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
  seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(fstat), 0);
  seccomp_load(ctx);
}

int main() {
  char c;
  int index;
  size_t bytes_read;
  puts("Are you fit to be the keeper of the zoo?");
  while (1) {
    puts("(f)ind a lion");
    puts("(l)ose a lion");
    puts("(v)iew a lion");
    scanf("%c%*c", &c);
    if (c=='f') {
      puts("idx:");
      scanf("%d%*c", &index);
      if ((index < 0) || (index > 16)) {exit(0);}
      mem[index] = (struct management*) malloc(sizeof(struct management));
      puts("len:");
      scanf("%d%*c", &mem[index]->size);
      mem[index]->ptr = (char*) malloc(mem[index]->size);
      strcpy(mem[index]->metadata, "valid management");
      puts("content:");
      read(0, mem[index]->ptr, mem[index]->size);
      (mem[index]->ptr)[mem[index]->size-1] = 0;
    }
    else if (c=='l') {
      puts("idx:");
      scanf("%d%*c", &index);
      if ((index < 0) || (index > 16)) {exit(0);}
      if (strncmp(mem[index]->metadata, "valid management", 16) != 0) { exit(0); }
      free(mem[index]);
      free(mem[index]->ptr);
      mem[index] = NULL;
    }
    else if (c=='v') {
      puts("idx:");
      scanf("%d%*c", &index);
      if ((index < 0) || (index > 16)) {exit(0);}
      if (strncmp(mem[index]->metadata, "valid management", 16) != 0) { exit(0); }
      puts(mem[index]->ptr);
    }
  }
}
