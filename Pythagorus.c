#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int main() 
{
	double side1, side2, a;
	scanf("%lf %lf", &side1, &side2);
	a = sqrt(pow(side1, 2) + pow(side2, 2)) ;
	printf("%lf", a);
	
	return 0;
}
