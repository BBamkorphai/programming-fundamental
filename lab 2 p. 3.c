#include <stdio.h>
int main()
{
	int input_num, i, j;
	printf("Enter your number: ");
	scanf("%d", &input_num);
	for ( i=0 ; i<input_num ; i++)
	{
		if ( i == 0 || i == input_num - 1)
		{
			for ( j=0; j<input_num ; j++)
			{
				printf("*");
			}
			printf("\n");
		}
		else
		{
			for ( j=0; j<input_num ; j++)
			{
				if ( j == 0 || j == input_num -1)
				{
					printf("*");
				}
				else
				{
					printf(" ");
				}
			}
			printf("\n");
		}
	}
	return 0;
}
