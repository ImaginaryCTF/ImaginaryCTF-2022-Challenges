#include <seccomp.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>

char buf[400];

void __attribute__ ((constructor)) setup() {
  setvbuf(stdout,NULL,2,0);
  setvbuf(stdin,NULL,2,0);
  scmp_filter_ctx ctx;
  ctx = seccomp_init(SCMP_ACT_KILL);
  seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(fstat), 0);
  seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 0);
  seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(openat), 0);
  seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);
  seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
  seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit_group), 0);
  seccomp_load(ctx);
}

int main() {
  puts("Welcome to Format Foolery!");
  puts("I'll print one, AND ONLY ONE, string for you.");
  puts("Enter your string below:");
  fgets(buf, 400, stdin);
  printf(buf);
}

int win() {
  if (strlen(buf)<8) {
    int fd;
    fd = open("flag.txt", 0);
    read(fd, buf, 50);
    write(1, buf, 50);
  }
}
