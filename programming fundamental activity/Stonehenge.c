#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int	abs(int nbr)
{
	if(nbr < 0)
		return (-nbr);
	else 
		return (nbr);
}
int main()
{
	//long long int x_point[1000], y_point[1000], distance[1000]; 
	int x_point[1000], y_point[1000], distance[1000]; 
	double test;
	double averagepoint_x = 0, averagepoint_y = 0; 
	int n,j;
	float sum_x=0, sum_y = 0;
	double	maxX, maxY, minX, minY;
	double	idx[4];
	double temp[2];
	double ignore;
	double chosen[8];
	int i,a,b,c;
	int value;
	scanf("%d", &n);
	printf("n is %d\n", n);
	// input
	for (i=0 ; i<n ; i++)
	{
		scanf("%d %d", &x_point[i], &y_point[i]);
		//printf("%ld %ld\n\n", x_point[i], y_point[i]);
	}
	for (i=0 ; i<n ; i++)
	{
		printf("%d %d", x_point[i], y_point[i]);
	}
	// find an average x and y
	for (i=0 ; i<n ; i++)
	{
		sum_x += x_point[i];
		sum_y += y_point[i];
	}
	averagepoint_x = sum_x/n ;
	averagepoint_y = sum_y/n ;
	printf("averagepoint_x is %f\n", sum_x/n);
	printf("averagepoint_y is %f\n", sum_y/n);
	//find longest distance between average point and other points
	for (i=0 ; i<n ; i++)
	{
		test = sqrt(pow((double)(averagepoint_x - x_point[i]),2) + pow((double)(averagepoint_y - y_point[i]),2));
		printf("distance %d is %f\n",i,test);
		int a = (int) test ;	
		printf("distance %d is %d\n",i,a);
		distance[i] = a;		
	}
	printf("+++++++++++\n");
	for (i=0 ; i<n ; i++)
	{
		printf("distance %d is %d\n",i,distance[i]);
	}
	for ( i = 0 ; i < n ; i++ )
	{
		value = distance[i];
		for ( j=i-1 ; j>= 0 ; j--)
		{
			if(distance[j]<= value)break;
			{
				distance[j+1]=distance[j];
			}
		}
		distance[j+1]=value;
	}
	printf("+++++++++++\n");
	for (i=0 ; i<n ; i++)
	{
		printf("distance %d is %d\n",i,distance[i]);
	}
	return 0;
	
}

