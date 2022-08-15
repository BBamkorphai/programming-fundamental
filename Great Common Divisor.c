#include <stdio.h>
int main()
{
	int a, b, i, fraction1, fraction2, GCD;
	scanf("%d %d", &a, &b);
	if ( a > b)
	{
		for ( i=1 ; i<=b ; i++)
		{
			fraction1 = a%i ;
			fraction2 = b%i ;
			if (fraction1 == 0 && fraction2 == 0 )
			{
				GCD = i;
			}
		}
	}
	else if ( a < b)
	{
		for ( i=1 ; i<=a ; i++)
		{
			fraction1 = b%i;
			fraction2 = a%i ;
			if (fraction1 == 0 && fraction2 == 0 )
			{
				GCD = i;
			}
		}
	}
	else if ( a==b )
	{
		GCD = a;
	}
	printf("%d", GCD);
}
