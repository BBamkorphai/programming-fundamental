#include <stdio.h>
#include <math.h>
int main()
{
	int n, i, j, a, b;
	scanf("%d", &n);
	a = 1;
	b = n+(n - 1);
	for ( i=1 ; i <= n ; i++)
	{
		for ( j=1 ; j <= n+(n-1); j++)
		{
			if ( j<=a || j>=b)
			{
				printf("* ");
			}
			else if ( j > a && j < b)
			{
				printf("  ");
			}
		}
		a++;
		b--;
		printf("\n");
	}
	a = a-2;
	b = b+2;
	for ( i=n+1 ; i <= 2*n-1 ; i++)
	{
		for ( j=1 ; j <= n+(n-1); j++)
		{
			if ( j<=a || j>=b)
			{
				printf("* ");
			}
			else if ( j > a && j < b)
			{
				printf("  ");
			}
		}
		a--;
		b++;
		printf("\n");
	}
}
