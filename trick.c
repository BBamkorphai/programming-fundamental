#include<stdio.h>
#include<string.h>


int main()
{
	int A;
	char inPut[100];
	scanf("%s", &inPut);
	int i;
	for ( i=0 ; i < strlen(inPut) ; i++)
	{
		if (inPut[i] == 'A' && A == 1)
			{
				A == 2;
			}
		else if ( inPut[i] == 'A' && A == 2)
			{
				A == 1;
			}
		else if ( inPut[i] == 'B' && A == 2)
			{
				A == 3;
			}
		else if ( inPut[i] == 'B' && A == 3)
			{
				A == 2;
			}
		else if ( inPut[i] == 'C' && A == 1)
			{
				A == 3;
			}
		else if( inPut[i] == 'A' && A == 3)
			;{
				A == 1;
			}
    }
    printf("%d", A);
}

