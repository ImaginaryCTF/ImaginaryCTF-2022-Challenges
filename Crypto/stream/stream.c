#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  if (argc < 3) {
    printf("[*] Usage: %s [FILE] [KEY] [OUT]\n", argv[0]);
    exit(-1);
  }

  long key = atol(argv[2]);
  FILE *fpt = fopen(argv[1], "r");
  fseek(fpt, 0, SEEK_END);
  int len = (ftell(fpt)/8+1)*8;
  fseek(fpt, 0, SEEK_SET);
  fclose(fpt);

  long *data = malloc(len);
  fgets(data, len, fpt);

  for (int i=0; i<len/8; i++) {
    data[i] = data[i] ^ key;
    key *= key;
  }

  FILE *fpc = fopen(argv[3], "w");
  fwrite(data, len, 1, fpc);
  fclose(fpc);
}
