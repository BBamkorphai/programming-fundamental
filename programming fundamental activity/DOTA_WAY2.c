#include<stdio.h>
long long int CNH(n,h)
{
    long long int result=1,HR=1,ans;
    for(int i=n;i>h;i=i-1)
	{
        result = result*i;
    }
    for(int j=1;j<=h;j=j+1)
	{ HR = HR*j;}
    ans = result / HR;
    printf("%lld",ans);
}
int main()
{
    unsigned long long int count=0;
    int n;
    scanf("%d",&n);
    (n%2)!=0 ? n+=1 : n ;
     int half = n/2;
     CNH(n,half);
    return 0;
}

