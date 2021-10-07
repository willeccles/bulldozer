#include <stdio.h>

int main(void) {
#ifdef COOL_MACRO
  puts("COOL_MACRO is defined");
#endif // COOL_MACRO
  puts(OUTPUT_STR);
  return 0;
}
