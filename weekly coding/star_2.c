#include <stdio.h>
#include <string.h>
int main()
{
    int n,i,j;
	char numbox[90][90];
    scanf("%d",&n);
    if (n%2==0)
    {
        int m=n-1,k=n/2;
        for(i=1 ; i<=n/2 ; i++)
        {
            for(j=1;j<=m;j++)
            {
                if (j==k || j==n-k) 
				{
					printf("*");
					numbox[i][j] = '*' ;
				}
                else 
				{
					printf("-");
					numbox[i][j] = '-' ;
				}
            }
            printf("\n");
            if(i<=n/2) 
			{
				k--;
			}
        }
        for ( i=n/2 ; i>=1 ; i--)
        {
        	for ( j=1 ; j<=m ; j++)
        	{
        		printf("%c", numbox[i][j]);
			}
			printf("\n");
		}
        
    }
    else
    {
        int m=n,k=n/2+1;
        for(i=1;i<=n/2+1;i++)
        {
            for(j=1;j<=m;j++)
            {
                if (j==k || j==n-k+1)
				{
					printf("*");
					numbox[i][j] = '*' ;	
				} 
                else 
                {
                	printf("-");
                	numbox[i][j] = '-' ;
				}
				
            }
            printf("\n");
            if(i<n/2+1) k--;
        }
        for ( i=n/2 ; i>=1 ; i--)
        {
        	for ( j=1 ; j<=m ; j++)
        	{
        		printf("%c", numbox[i][j]);
			}
			printf("\n");
		}
    }
}
