#include <stdio.h>
int main()
{
	int day, month, daycount = 0, i, ans;
	scanf("%d %d", &day, &month);
	daycount = daycount + day;
	if( month>1 )
	{
        for ( i=1 ; i<month ; i++ )
		{
            if(i==1 || i==3 || i==5 || i==7 || i==8 || i==10 || i==12)
			{
                daycount += 31;
            }
			else if ( i==4 || i==6 || i==9 || i==11 )
			{
                daycount += 30;
            }else if ( i==2 )
			{
                daycount += 28;
            }
        }
    }
	else if ( month == 1 )
	{
        daycount += 0;
    }
	ans = daycount%7;
	switch(ans)
	{
		case 0:
			printf("Wednesday");
			break;
		case 1:
			printf("Thursday");
			break;
		case 2:
			printf("Friday");
			break;
		case 3:
			printf("Saturday");
			break;
		case 4:
			printf("Sunday");
			break;
		case 5:
			printf("Monday");
			break;
		case 6:
			printf("Tuseday");
			break;
	}
	return 0;
	
}
