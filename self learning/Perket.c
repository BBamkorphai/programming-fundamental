#include <stdio.h>
#include <stdlib.h>
int n, p[10][2], m=1000000000;
void combi(int s, int b, int i) {
  // printf("%d %d\n", s, b);
  if (i == n) {
    if (b != 0 && abs(s-b) < m) { // b != 0 (empty set)
      m = abs(s-b);
    }
  }
  else  {
    combi(s, b, i+1);
    combi(s*p[i][0], b+p[i][1], i+1);
  }
}
int main(void) {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d %d", &p[i][0], &p[i][1]);
  }
  combi(1, 0, 0);
  printf("%d", m);
  return 0;
}
