#include <stdio.h>
int main()
{
	int i,n, j, Adirancount = 0, Brunocount = 0, Gorancount = 0, value;
	char answer[100], AdiranArray[100], BrunoArray[100], GoranArray[100], score[3];
	scanf("%d", &n);
	scanf("%s", answer);
	for ( i=0 ; i<n ; i++)
	{
		if( i%3 == 0)
		{
			AdiranArray[i] = 'A';
		}
		else if( i%3 == 1)
		{
			AdiranArray[i] = 'B';
		}
		else if( i%3 == 2)
		{
			AdiranArray[i] = 'C';
		}
				
	}
	for ( i=0 ; i<n ; i++)
	{
		if( i%4 == 0)
		{
			BrunoArray[i] = 'B';
		}
		else if( i%4 == 1)
		{
			BrunoArray[i] = 'A';
		}
		else if( i%4 == 2)
		{
			BrunoArray[i] = 'B';
		}
		else if( i%4 == 3)
		{
			BrunoArray[i] = 'C';
		}	
	}
	for ( i=0 ; i<n ; i++)
	{
		if( i%6 == 0)
		{
			GoranArray[i] = 'C';
		}
		else if( i%6 == 1)
		{
			GoranArray[i] = 'C';
		}
		else if( i%6 == 2)
		{
			GoranArray[i] = 'A';
		}
		else if( i%6 == 3)
		{
			GoranArray[i] = 'A';
		}
		else if( i%6 == 4)
		{
			GoranArray[i] = 'B';
		}
		else if( i%6 == 5)
		{
			GoranArray[i] = 'B';
		}		
	}
	for ( i=0 ; i<n ; i++)
	{
		if ( AdiranArray[i] == answer[i])
		{
			Adirancount++ ;
		}
		if ( BrunoArray[i] == answer[i])
		{
			Brunocount++ ;
		}
		if ( GoranArray[i] == answer[i])
		{
			Gorancount++ ;
		}
	}
	score[0] = Adirancount;
	score[1] = Brunocount;
	score[2] = Gorancount;
	for ( i = 0 ; i < 3 ; i++ )
	{
		value = score[i];
		for ( j=i-1 ; j>= 0 ; j--)
		{
			if(score[j]<= value)break;
			{
				score[j+1]=score[j];
			}
		}
		score[j+1]=value;
	}
	printf("%d\n", score[2]);
	if ( Adirancount == score[2])
	{
		printf("Adrian\n");
	}
	if ( Brunocount == score[2])
	{
		printf("Bruno\n");
	}
	if( Gorancount == score[2])
	{
		printf("Goran\n");
	}
}
