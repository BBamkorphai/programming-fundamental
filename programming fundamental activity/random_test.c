#include<stdio.h>
#include<windows.h>
#include <time.h>
int main()
{
	int i, n=1, ran_num;
	srand(time(NULL));
	while ( n!= 10)
	{
		ran_num = (rand()% 80);
		printf("%d\n",ran_num);
		n++;
	}		
	return 0;
}
