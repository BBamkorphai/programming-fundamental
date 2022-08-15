#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() 
{
	char str[10000] ;
	scanf("%s", &str);
	int i;
	int sum1 = 0 ;
	int sum2 = strlen(str) ;
	for( i = 0; i < strlen(str); i++)
	{
		if(str[i]>= 'a' && str[i] <= 'z')
		{
			sum1++;
		}
	}
	if ( sum1 == 0)
	{
		printf("All Capital Letter");
	}
	else if ( sum1 != sum2 )
	{
		printf("Mix");
	}
	else
	{
		printf("All Small Letter");
	}
	return 0;
}
