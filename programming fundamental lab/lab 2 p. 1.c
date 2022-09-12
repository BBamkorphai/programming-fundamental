#include<stdio.h>
#include<math.h>
int main()
{
	int num, a, i, b, sum = 1;
	printf("Enter your number:");
	scanf("%d", &num);
	printf("\n");
	// num = stable variable
	a = num;
	printf("Factory result:");
		for ( i=2 ; i <= num; i++)
		{
			if ( a%i == 0)
			{
				printf("%d", i);
				a = a/i;
				sum = i*sum;
				if ( sum != num)
				{
					printf(" x ");
				}
				while ( a%i == 0)
				{
					a = a/i;
					sum = i*sum;
					printf("%d", i);
					if ( sum != num)
					{
						printf(" x ");
					}
				}
			}
		}
		printf("\nsum is %d", sum);
	return 0;
}
