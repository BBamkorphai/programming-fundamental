#include <stdio.h>
//0022 : star
int main()
{
    int n,i,j;
    scanf("%d",&n);
    if (n%2==0)
    {
        int m=n-1,k=n/2;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                if (j==k || j==n-k) printf("*");
                else printf("-");
            }
            printf("\n");
            if(i<=n/2) k--;
            if(i>=n/2) k++;
        }
    }
    else
    {
        int m=n,k=n/2+1;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                if (j==k || j==n-k+1) printf("*");
                else printf("-");
            }
            printf("\n");
            if(i<n/2+1) k--;
            if(i>=n/2+1) k++;
        }
    }
}
