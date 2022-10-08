#include<stdio.h>
int main()
{
	FILE* fp;
	struct cat{
	int level; 
	int score;
	char name[50];
	};
	struct cat dog[5];
	int i;
	fp = fopen("mytest.txt", "a");
	for ( i=0 ; i<5 ; i++)
	{
		printf("Input name: level: score:");
		scanf("%s %d %d", &dog[i].name, &dog[i].level, &dog[i].score);
	}
	for ( i=0 ; i<5 ; i++)
	{
		fprintf(fp, "name:%s level:%d score:%d\n", dog[i].name, dog[i].level, dog[i].score);
	}
	fclose(fp);
	return 0;
}
