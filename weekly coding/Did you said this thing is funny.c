#include <stdio.h>
#include <math.h>
#include <string.h>
int main()
{
	int num, array_Input[1002], i , pre_var , post_var, j, k, checker = 1;
	printf("number of digits: ");
	scanf("%d/n", &num);
	if (num <= 0)
	{
		printf("ERROR! number of digits must be integer that > 0");
		return 0;
	}
	
	printf("Those number are:");
	for ( i=0 ; i<num ; i++)
	{
		scanf("%d", &array_Input[i]);
		if (array_Input[i] < 0 || array_Input[i] >= 10)
		{
			printf("ERROR! number must be integer that >= 0 and <=9");
			return 0;
		}
	}
	// number arrangment
	for ( i=0 ; i<num ; i++)
	{
		pre_var = array_Input[i];
		for ( j=i-1 ; j>= 0 ; j--)
		{
			if (array_Input[j] <= pre_var)break;
			{
				array_Input[j+1] = array_Input[j];
			}
		}
		array_Input[j+1] = pre_var ;
	}
	
	// print first number
	for ( i=0 ; i<num ; i++)
	{
		if ( checker == 1 && array_Input[i] != 0)
		{
			printf("%d", array_Input[i]);
			array_Input[i] = -1;
			checker = 0;
		}
	}
	
	//print other number
	for ( i=0 ; i<num ; i ++)
	{
		if ( array_Input[i] >= 0)
		{
			printf("%d", array_Input[i]);
		}
	}
	return 0;
	
	
}

