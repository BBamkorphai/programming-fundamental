#include<stdio.h>
int main()
{
	int a, i, j, n, b;
	scanf("%d %d", &a, &b);
	// a = high b = lengh
	if ( a < 3 || b < 3)
	{
		printf("ERROR!");
	}
	else
	{
		for(i=0 ; i<a ; i++)
		{
			for ( j=0 ; j<b ; j++)
			{
				if ( i%2 == 0)
				{
					if (j%2 == 0)
					{
						printf("O");
					}
					else if (j%2 == 1)
					{
						printf("X");
					}
				}
				if ( i%2 == 1)
				{
					if (j%2 == 0)
					{
						printf("X");
					}
					else if (j%2 == 1)
					{
						printf("O");
					}
				}	
			}
		printf("\n");
		}
	}
	return 0;
}
