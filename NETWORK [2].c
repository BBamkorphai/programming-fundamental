#include<stdio.h>
#include<math.h>
int main() {
  int n, x, host;
  scanf("%d", &x);
  if ( x >= 24 && x <= 30)
  {
    n = 32 - x;
    host = (pow(2,n)) - 2;
    printf("%d", host);
  }
  if ( x < 24 || x > 30)
  {
  	printf("error");
  }
 return 0;
}
