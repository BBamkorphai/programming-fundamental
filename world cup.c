# include <stdio.h>
int main()
{
	int score[4][4], i, j, teamscore[4] = {0, 0, 0, 0}, shootingscore[4] = {0, 0, 0, 0}, shootedscore[4] = {0, 0, 0, 0}, value, teamscore2[4] = {0, 0, 0, 0};
	char team[4];
	// input
	for ( i=0 ; i<4 ; i++)
	{
	scanf("%s", &team[i]);
	}
	for ( i=0 ; i<4 ; i++)
	{
		for ( j=0 ; j<4 ; j++)
		{
			scanf("%d", &score[i][j]);
		}
	}
	
	
	for ( i=0 ; i<4 ; i++)
	{
	printf("%s\n", team[i]);
	}
	
	
	
	printf("\n\n\n");
	
	
	
	for ( i=0 ; i<4 ; i++)
	{
		for ( j=0 ; j<4 ; j++)
		{
			if ( j>i )
			{
				if ( score[i][j] == score[j][i])
				{
					teamscore[i] += 1;
					teamscore[j] += 1;
					teamscore2[i] += 1;
					teamscore2[j] += 1;
				}
				else if ( score[i][j] > score[j][i])
				{
					teamscore[i] += 3;
					teamscore2[i] += 3;
				}
				else if ( score[i][j] < score[j][i])
				{
					teamscore[j] += 3;
					teamscore2[j] += 3;
				}
			}
			else continue;
		}
	}
	for ( i=0 ; i<4 ; i++)
	{
		printf("Team's scores are %d\n", teamscore[i]);
	}
	
	printf("\n\n\n\n");
	for ( i=0 ; i<4 ; i++)
	{
		for ( j=0 ; j<4 ; j++)
		{
			shootingscore[i] += score[i][j];
		}
		printf("shootingscores are %d\n", shootingscore[i]);
	}
	printf("\n\n\n\n");
	for ( i=0 ; i<4 ; i++)
	{
		for ( j=0 ; j<4 ; j++)
		{
			shootedscore[i] += score[j][i];
		}
		printf("shootedscores are %d\n", shootedscore[i]);
	}
	
	for ( i = 0 ; i < 4 ; i++ )
	{
		value = teamscore[i];
		for ( j=i-1 ; j>= 0 ; j--)
		{
			if(teamscore[j]<= value)break;
			{
				teamscore[j+1]=teamscore[j];
			}
		}
		teamscore[j+1]=value;
	}
	for ( i = 0 ; i < 4 ; i++ )
	{
		printf("%d\t", teamscore[i]);
	}
	printf("\n\n\n");
	for ( i=0 ; i<4 ; i++)
	{
		printf("Team's scores are %d\n", teamscore[i]);
	}
	printf("\n\n\n");
	for ( i=3 ; i>=0 ; i--)
	{	
		if ( teamscore[i] == teamscore2[0])
		{
			printf("%s %d", team[0], teamscore[i]);
		}
		else if ( teamscore[i] == teamscore2[1])
		{
			printf("%s %d", team[1], teamscore[i]);
		}
		else if ( teamscore[i] == teamscore2[2])
		{
			printf("%s %d", team[2], teamscore[i]);
		}
		else if ( teamscore[i] == teamscore2[3])
		{
			printf("%s %d", team[3], teamscore[i]);
		}
		printf("\n");		
	}
}
