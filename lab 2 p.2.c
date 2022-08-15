#include <stdio.h>
int main()
{
	int a, b, c, i, fraction1, fraction2, GCD;
	printf("Enter your frist number: ");
	scanf("%d", &a);
	printf("Enter your second number: ");
	scanf("%d", &b);
	if ( a < b)
	{
		c = a;
	}
	else
	{
		c = b;
	}
	for ( i=1 ; i<=c ; i++)
	{
		fraction1 = a%i ;
		fraction2 = b%i ;
		if (fraction1 == 0 && fraction2 == 0 )
		{
			GCD = i;
		}
	}
	printf("Greatest common divisor is %d", GCD);
	return 0;
}
