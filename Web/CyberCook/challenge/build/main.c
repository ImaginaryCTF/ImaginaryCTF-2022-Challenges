#include <emscripten.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char *c;
static char *decoding_table = NULL;
static int mod_table[] = {0, 2, 1};

int EMSCRIPTEN_KEEPALIVE idx(char ch) {
  for (int i=0; i<sizeof(c); i++) {
    if (ch==c[i]) { return i; }
  }
  return 0;
}

__attribute__((constructor)) int EMSCRIPTEN_KEEPALIVE init_conv() {
  c = malloc(0x3010);
  strcpy(c, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+");
  return 0;
}


int hexchr2bin(const char hex, char *out)
{
	if (out == NULL)
		return 0;

	if (hex >= '0' && hex <= '9') {
		*out = hex - '0';
	} else if (hex >= 'A' && hex <= 'F') {
		*out = hex - 'A' + 10;
	} else if (hex >= 'a' && hex <= 'f') {
		*out = hex - 'a' + 10;
	} else {
		return 0;
	}

	return 1;
}

size_t hexs2bin(char *hex, unsigned char *out)
{
	size_t len;
	char   b1;
	char   b2;
	size_t i;

	if (hex == NULL || *hex == '\0' || out == NULL)
		return 0;

	len = strlen(hex);
	if (len % 2 != 0)
		len--;
	len /= 2;

//	memset(out, '\0', len);
	for (i=0; i<len; i++) {
		if (!hexchr2bin(hex[i*2], &b1) || !hexchr2bin(hex[i*2+1], &b2)) {
			return 0;
		}
		out[i] = (b1 << 4) | b2;
	}
	return len;
}

char EMSCRIPTEN_KEEPALIVE *base64_encode(unsigned char *data, size_t input_length) {
    char *encoded_data = malloc(input_length);
    hexs2bin(data, data);
    char **out = malloc(32);
    *out = encoded_data;
    if (encoded_data == NULL) return NULL;
    for (int i = 0, j = 0; i < input_length;) {
        uint32_t octet_a = i < input_length ? (unsigned char)data[i++] : 0;
        uint32_t octet_b = i < input_length ? (unsigned char)data[i++] : 0;
        uint32_t octet_c = i < input_length ? (unsigned char)data[i++] : 0;
        uint32_t triple = (octet_a << 0x10) + (octet_b << 0x08) + octet_c;
        encoded_data[j++] = c[(triple >> 3 * 6) & 0x3F];
        encoded_data[j++] = c[(triple >> 2 * 6) & 0x3F];
        encoded_data[j++] = c[(triple >> 1 * 6) & 0x3F];
        encoded_data[j++] = c[(triple >> 0 * 6) & 0x3F];
    }
    return *out;
}
