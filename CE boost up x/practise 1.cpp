#include <stdio.h>
int main()
{
	int x, y, A;
	scanf("%d", &A);
	for ( x=1 ; x<=A ; x++)
	{
		for( y=0 ; y<x ; y++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
