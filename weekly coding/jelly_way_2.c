#include <stdio.h>
int main()
{
	int count = 0, i, num;
	printf("size of jelly is: ");
	for ( i=0 ; i<3 ; i++)
	{
		scanf("%d", &num);
		while ( num != 1)
		{
			if ( num % 2 != 0)
			{
				num--;
			}
			num /= 2;
			count++;
		}
	}
	if ( count > 1)
	{
		printf("You must chop it %d times.", count);
	}
	if ( count == 1)
	{
		printf("You must chop it %d time.", count);
	}
	if ( count == 0)
	{
		printf("You don't have to chop it.");
	}
	return 0;
}
