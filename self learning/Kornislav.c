#include <stdio.h>
int main()
{
	int i, j, array[4], value;
	scanf("%d", &array[0]);
	scanf("%d", &array[1]);
	scanf("%d", &array[2]);
	scanf("%d", &array[3]);
	for ( i = 0 ; i < 4 ; i++ )
	{
		value = array[i];
		for ( j=i-1 ; j>= 0 ; j--)
		{
			if(array[j]<= value)break;
			{
				array[j+1]=array[j];
			}
		}
		array[j+1]=value;
	}
	printf("%d", array[2]*array[0]);
}
