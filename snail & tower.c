#include<stdio.h>
#include <math.h>
int main() 
{
 float a, b, h;
  scanf("%f %f %f", &a, &b, &h);
  printf("%d",(int)ceil(h/(a-b)));
   
 
 return 0;
}
