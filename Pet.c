#include <stdio.h>
int main () 
{
	int i, a, b, c, d, array[5], most_sum = 0, all;
	
	for ( i=0 ; i<5 ; i++ )
	{
		scanf("%d %d %d %d", &a, &b, &c, &d);
		all = a+b+c+d;
		array[i] = all;
		if ( all>most_sum )
		{
			most_sum = all ;
		}
	}
	for ( i=0 ; i<5 ; i++ )
	{
		if ( array[i] == most_sum)
		{
			printf("%d %d", i+1, most_sum);
		}
	}
}
