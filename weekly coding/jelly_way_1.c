#include <stdio.h>
int main()
{
	int jelly_size[3];
	int i, j, count = 0;
	printf("size of jelly is: ");
	scanf("%d %d %d", &jelly_size[0], &jelly_size[1], &jelly_size[2]);
	while ( jelly_size[0] != 1 || jelly_size[1] != 1 || jelly_size[2] != 1 )
	{
		for ( i=0 ; i<3 ; i++)
		{
			if ( jelly_size[i] % 2 !=0 && jelly_size[i] != 1)
			{
				jelly_size[i]--;
				// all fixed
			}
		}
		for ( i=0 ; i<3 ; i++)
		{
			if ( jelly_size[i] % 2 ==0 && jelly_size[i] != 1)
			{
				while ( jelly_size[i] != 1)
				{
					jelly_size[i] /= 2;
					count++;
				}
			}
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
