#include <stdio.h>
#include <math.h>
int main()
{
	int n, array[100][100], i, j, count=0, flag=0, sum=0, a=0, b=0;
	scanf("%d",&n);
	for ( i=0 ; i<n ; i++)
	{
		for ( j=0 ; j<n ; j++ )
		{
			scanf("%d",&array[i][j]);
		}
	}
	//flag
	for ( i=0 ; i<n ; i++)
	{
		flag += array[i][0];
	}
	//horizontal check
	for ( i=0 ; i<n ; i++)
	{
		for ( j=0 ; j<n ; j++ )
		{
			sum += array[i][j];
		}
		if ( sum == flag)
		{
			count+=1;
		}
		sum = 0;
	}
	//vertical check
	for ( i=0 ; i<n ; i++)
	{
		for ( j=0 ; j<n ; j++ )
		{
			sum += array[j][i];
		}
		if ( sum == flag)
		{
			count+=1;
		}
		sum = 0;
	}
	//diagonal check line 1
	for ( i=0 ; i<n ; i++)
	{
		sum += array[a][b];
		a+=1;
		b+=1;
	}
	if ( sum == flag)
	{
		count+=1;
	}
	sum = 0;
	//diagonal check line 2
	a=n-1;
	b=n-1;
	for ( i=n ; i>0 ; i--)
	{
		sum += array[a][b];
		a-=1;
		b-=1;
	}
	if ( sum == flag)
	{
		count+=1;
	}
	sum = 0;
	if (count == (n*2)+2)
	{
		printf("Yes");
	}
	else
	{
		printf("No");
	}
	return 0;
	
}
