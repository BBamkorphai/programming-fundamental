#include <stdio.h>
#include <math.h>
int main() {
    int n, i, j, k;
	scanf("%d", &n);
	for(i = 1; i <= n - 1; i++) 
	{
		for(j = 1; j <= i; j++)
		{
			printf("* ");
		}
		for(k = 1; k <= 2 * (n - i); k++)
		{
			printf("  ");
		}
		for(j = i; j >= 1; j--)
		{
			printf("* ");
		}
	}
	for(i = n; i >= 1; i--) 
	{
		for(j = 1; j <= i; j++)
		{
			printf("* ");
		}
		for(k = 1; k <= 2 * (n - i); k++)
		{
			printf("  ");
		}
		for(j = i; j >= 1; j--)
		{
			printf("* ");
		}
	}
    return 0;
}
