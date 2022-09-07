#include<stdio.h>
#include<math.h>
void is_prime_number(int);
int main()
{
	int n;
	printf("This number is Prime or not:\n");
	scanf("%d",&n);
	is_prime_number(n);
	return 0;

}
void is_prime_number(int num_input)
{
	int i,checker = 0;
	for ( i=2 ; i<num_input ; i++)
	{
		if ( num_input%i == 0)
		{
			checker = i;
		}
	}
	if ( checker != 0)
	{
		printf("%d is not prime number", num_input);
	}
	else if ( checker == 0 )
	{
		printf("%d is prime number", num_input);
	}
}
