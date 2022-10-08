#include <stdio.h>
#include <math.h>
int main()
{
	int array[10];
	int i;
	for ( i=0 ; i<10 ; i++)
	{
		scanf("%d",&array[i]);
	}
	for ( i=1 ; i<9 ; i++)
	{
		if ( array[i-1] % 2 != 0 && array[i+1] % 2 != 0)
		{
			printf("%d \n",array[i]);
		}
	}
	return 0;
}
