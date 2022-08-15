#include <stdio.h>
int main()
{
	int i,a,sum = 0, fraction,j ;
	int array[9] = {};
	for ( i=0 ; i<9 ; i++)
	{
		scanf("%d", &a);
		array[i] = a;
		sum += a;
	}
	fraction = sum-100;
	for ( i=0 ; i<9 ; i++)
	{
		for ( j=0 ; j<9 ; j++)
		{
			if (array[i] == array[j])
			{
				continue;
			}
			if (array[i]+array[j] == fraction)
			{
				array[i] = 0;
				array[j] = 0;
				for ( i=0 ; i<9 ; i++)
				{
					if (array [i] != 0)
					{
							printf("%d\n", array[i]);
					}
				}
			}	
		}
	}
}
