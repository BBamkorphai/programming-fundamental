#include <stdio.h>
int swap ( int*a, int*b)
{
	int flag ;
	flag = *a;
	*a = *b;
	*b = flag;
}
int main()
{
	int a,b;
	scanf("%d %d", &a, &b);
	swap(&a,&b);
	printf_s("%d %d", a,b);
	return 0;
	
}


