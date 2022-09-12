#include <stdio.h>
int main()
{
	int n, i, j, count = 0;
	for ( i=1 ; i <= 10000 ; i++)
	{
		count = 0;
		for ( j=1 ; j <= i-1 ; j++)
		{
			if ( i%j == 0)
			{
				count += j;
			}
		}
		if ( count == i )
		{
			printf("%d ", count);
		}
	}
	return 0;
}
