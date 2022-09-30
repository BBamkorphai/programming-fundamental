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
	int x_point[1000], y_point[1000], distance,averagepoint_x = 0, averagepoint_y = 0, n, sum_x , sum_y;
	int	maxX, maxY, minX, minY;
	int	idx[4];
	int temp[2];
	int ignore;
	int chosen[8];
	scanf("%d", &n);
	// input
	for ( i=0 ; i<=n ; i++)
	{
		scanf("%d %d", &x_point[i], &y_point[i]);
	}
	
	// find an average x and y
	for ( i=0 ; i<=n ; i++)
	{
		sum_x += x_point[i];
		sum_y += y_point[i];
	}
	averagepoint_x = sum_x/n ;
	averagepoint_y = sum_y/n ;
	i = 0;
	/*minX = averagepoint_x;
	maxX = averagepoint_x;
	minY = averagepoint_y;
	maxY = averagepoint_y;*/
	minX = 0;
	maxX = 0;
	minY = 0;
	maxY = 0;
	while (i <= n)
	{
		if(x_point[i] < minX)
		{
			minX = x_point[i];
			idx[0] = i;
		}
		if(x_point[i] > maxX)
		{
			maxX = x_point[i];
			idx[1] = i;
		}
		if(y_point[i] < minY)
		{
			minY = y_point[i];
			idx[2] = i;
		}
		if(y_point[i] < maxY)
		{
			maxY = y_point[i];
			idx[3] = i;
		}
		i++;
	}
	/*i = 0;
	temp[0] = abs(x_point[idx[i]]) + abs(y_point[idx[i]]);
	while (i < 4)
	{
		if(abs(x_point[idx[i]]) + abs(y_point[idx[i]]) < temp)
		{
			temp[0] = abs(x_point[idx[i]]) + abs(y_point[idx[i]]);
			temp[1] = i;
		}
		i++;
	}
	ignore = temp[1];*/
	i = 0;
	while (i < 4)
	{
		/*if(i == ignore)
			ignore = ignore;
		else
		{
			chosen[i*2] = x_point[idx[i]];
			chosen[(i*2) + 1] = y_point[idx[i]];
		}*/
		chosen[i*2] = x_point[idx[i]];
		chosen[(i*2) + 1] = y_point[idx[i]];
		i++;
	}
}
