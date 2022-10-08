#include <stdio.h>
#include <math.h>
int main()
{
	int array[10],checker[10];
	int i;
	for ( i=0 ; i<10 ; i++)
	{
		scanf("%d",&array[i]);
		if ( array[i] % 2 == 0)
		{
			checker[i] = 0;
		}
		else if(array[i] % 2 != 0)
		{
			checker[i] = 1;
		}	
	}
	for ( i=0 ; i<10 ; i++)
	{
		printf("%d",checker[i]);
	}
	printf("\n\n");
	for ( i=0 ; i<10 ; i++)
	{
		if ( checker[i] + checker[i+2] == 2)
		{
			printf("%d \n",array[i+1]);
		}
	}
	return 0;
}
