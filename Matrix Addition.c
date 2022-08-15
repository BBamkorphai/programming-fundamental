#include <stdio.h>
#include <stdlib.h>
int main() 
// m = y
// n = x
{
	int m, n, a[100][100], b[100][100], c[100][100], i, j;
	scanf("%d %d", &m,&n);
	for ( i=0 ; i<m ; i++){
		for ( j=0 ; j <n ; j++){
			scanf("%d", &a[i][j]);
			
		}
	}
	for ( i=0 ; i<m ; i++){
		for ( j=0 ; j <n ; j++){
			scanf("%d", &b[i][j]);
			
		}
	}
	for ( i=0 ; i<m ; i++)
	{
		for ( j=0 ; j <n ; j++)
		{
			
			printf("%d\t", a[i][j] + b[i][j]);
		}
	printf("\n");
	}
	return 0;
}
