#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main()
{
	//long long int x_point[1000], y_point[1000], distance[1000]; 
	int x_point[1000], y_point[1000], distance[1000][2]; 
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
	int area;
	int sum_all;
	double answer;
	double last_answer;
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
		printf("point %d is (%d,%d)\n", i,x_point[i], y_point[i]);
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
		distance[i][0] = a;	
		distance[i][1] = i;		
	}
	printf("+++++++++++\n");	
	//int j;
	for (i= 0; i< n; ++i) {
		for (j= 0; j< n; ++j) {
			if (distance[i][0] > distance[j][0]) {
				int hold[2] = {distance[i][0], distance[i][1]};
				
				distance[i][0] = distance[j][0];
				distance[i][1] = distance[j][1];
				
				distance[j][0] = hold[0];
				distance[j][1] = hold[1];
			}
		}
	}
	
	
	for (i=0 ; i<n ; i++)
	{
		printf("distance[1] %d is %d\n",i,distance[i][0]);
		printf("distance[2] %d is %d\n",i,distance[i][1]);
	}
	
	//area
	a = distance[0][1];
	b = distance[1][1];
	c = distance[2][1];
	sum_all = (x_point[a]*y_point[b]) + (x_point[b]*y_point[c]) + (x_point[c]*y_point[a]) - (y_point[a]*x_point[b]) - (y_point[b]*x_point[c]) - (y_point[c]*x_point[a]);
	printf("sumall is %d\n",sum_all);
	
	area = abs(sum_all);
	printf("area is %d\n", area);
	//answer = (double) area ;
	//printf("answer is %f\n", answer);
	printf("last_answer is %f\n",area/2.0);
	return 0;
	
}

