#include <stdio.h>
int main()
{
	int i , j, k = 1, nI, nMax, array1[1001], array2[1001];
	scanf("%d", &nMax);
	scanf("%d", &nI);
	array2[0] = 2;
	for ( i=0 ; i<=nMax-2 ; i++)
	{
		array1[i] = i+2;
//		printf("%d ",array1[i]);
	}
	
	for ( i=0 ; i<=nMax-1 ; i++)
	{
		if ( array1[i] == 0)
		{
			continue ;
		}
		if ( array1[i] != 0)
		{
			int aaa = array1[i];
			for ( j=1 ; j<=nMax-1 ; j++)
			{
				if ( array1[j] == 0)
				{
					continue ;
				}
				if ( array1[j] != 0)
				{
					if ( array1[j]%aaa == 0)
					{
						array2[k] = array1[j] ;
						k++;
						array1[j] = 0;
					}
				}
			}
		}
	}
	printf("%d", array2[nI-1]);
}
