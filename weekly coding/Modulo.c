#include <stdio.h>
int main()
{
	int array[20] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, };
	int a, i, j, num, count = 0, checker = 0;
	for ( i=0 ; i<10 ; i++)
	{
		scanf("%d", &a);
		num = a%42 ;
		for ( j=0 ; j<10 ; j++)
		{
			if (num != array[j] )
			{
			
			}
			else if (num == array[j] )
			{
				checker = 1;
				break;
			}
		}
		if (checker == 0)
		{
			array[i] = num;
			count ++;
		}
		checker = 0;
	}
	printf("%d", count);
}
