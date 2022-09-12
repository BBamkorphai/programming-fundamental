#include <stdio.h>
int main()
{
	int fraction[10];
	int i,j,k,n,frac1, a=0;
	for ( i=0 ; i<10 ; i++)
	{
		scanf("%d", &n);
		frac1 = n%42;
		for ( j=0 ; j<10 ; j++)
		{
			if ( frac1 != fraction[j])
			{
				a++;
				fraction[i] = frac1 ;
			}
			
		}	
	}
	printf("%d",a);
	return 0;
	
}
