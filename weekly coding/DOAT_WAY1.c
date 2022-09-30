#include <stdio.h>
int main()
{
	long long int n, r, n_fac, r_fac, i, result, flag;
	scanf("%d", &n);
	if ( n == 1)
	{
		printf("2");
	}
	else if ( n%2 == 0)
	{
		r = n/2 ;
		flag = r;
		n_fac = 1;
		r_fac = 1;
		for (i=1 ; i<=r ; i++)
		{
			n_fac *= n;
			n-=1;
		}
		for (i=1 ; i<=flag ; i++)
		{
			r_fac *= r;
			r-=1 ;
		}
		result = n_fac/r_fac;
		printf("%lld",result);
	}
	else if ( n%2 != 0)
	{
		r = (n/2)+1 ;
		flag = r;
		n_fac = 1;
		r_fac = 1;
		for (i=1 ; i<=r ; i++)
		{
			n_fac *= n;
			n-=1;
		}
		for (i=1 ; i<=flag ; i++)
		{
			r_fac *= r;
			r-=1 ;
		}
		result = n_fac/r_fac;
		printf("%lld",result*2);
	}
	return 0;
}
