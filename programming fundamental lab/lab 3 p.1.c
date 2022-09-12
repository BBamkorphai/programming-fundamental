#include <stdio.h>
#include <math.h>
int main()
{
	int a, b = 0, c, ans=100;
	scanf("%d", &a);
	while ( ans > 10 )
	{
		b = 0;
		while ( a>10 )
		{
			c = a % 10;
			b += c;
			a = floor(a/10);
			if(a<10)
			{
				b+=a;
			}
		}
		a = b;
		ans = b;
	}
	printf("ans is %d", ans);
}
