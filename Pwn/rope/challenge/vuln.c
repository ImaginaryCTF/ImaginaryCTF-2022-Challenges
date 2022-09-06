#include <seccomp.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>

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

char inp[256];

int main() {
  long *where;
  long what;
  printf("%p\n", &puts);
  fgets(inp, 256, stdin);
  scanf("%ld%*c", &where);
  scanf("%ld%*c", &what);
  *where = what;
  puts("ok");
}
