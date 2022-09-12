#include<stdio.h>
#include<string.h>
int main(){
    int day,month,countday,ans,i;
    char Day[][7] = {"Wednes","Thurs","Fri","Satur","Sun","Mon","Tues"};
    scanf("%d %d", &day, &month);
    countday = day;
    if(month>1)
	{
        for(i=1; i<month; i++)
		{
            if(i==1 || i==3 || i==5 || i==7 || i==8 || i==10 || i==12)
			{
                countday += 31;
            }
			else if(i==4 || i==6 || i==9 || i==11)
			{
                countday += 30;
            }
			else if(i==2)
			{
                countday += 28;
            }
        }
    }
	else if(month==1)
	{
        countday += 0;
    }
    ans = countday%7;
    printf("%sday", Day[ans]);
}
