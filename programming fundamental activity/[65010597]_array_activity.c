#include <stdio.h>
#include <string.h>
int main()
{
	char boxInput[100];
	int i;
	scanf("%s", boxInput);
	for( i=0 ; i<strlen(boxInput) ; i++)
	{
		if ( boxInput[i] >= 'A' && boxInput[i] <= 'Z')
		{
			printf("%c", boxInput[i]);
		}
	}
	return 0;
}
