#include <stdio.h>
int main()
{
	int a, result;
	printf("Input your score: ");
	scanf("%d", &a);
	result = a/10 ;
	switch(result)
	{
		case 10:
		case 9:
		case 8:
			printf("your grade is A");
			break;
		case 7:
			printf("your grade is B");
			break;
		case 6:
			printf("your grade is C");
			break;
		case 5:
			printf("your grade is D");
			break;
		case 4:
		case 3:
		case 2:
		case 1:
		case 0:
			printf("your grade is F");
			break;
		default:
			printf("Invalid score");
	}
}
