#include<stdio.h>
#include<math.h>
int main() 
{
  float mass , result;
  int result2, fuel;
  scanf("%f", &mass);
  printf("mass is %f\n", mass);
  result = ( mass/3 );
  printf("result is %f\n", result);
  result2 = floor(result);
  printf("result2 is %d\n", result2);
  fuel = result - 2;
  if ( fuel <= 0)
  {
  	fuel = 0;
  }
  printf("%d", fuel);
  return 0;
}
