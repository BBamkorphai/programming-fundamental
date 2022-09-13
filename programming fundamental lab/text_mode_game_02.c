#include<stdio.h>
#include<windows.h>
#include<conio.h>
void draw_ship (int x,int y)
{
	COORD c = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE) , c);
	printf(" <-0-> ");
}
void erase_ship(int x,int y)
{
	COORD c = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE) , c);
	printf("       ");
}
void setcursor(int visible)
{
	HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
	CONSOLE_CURSOR_INFO lpCursor;
	lpCursor.bVisible = visible;
	lpCursor.dwSize = 20;
	SetConsoleCursorInfo(console,&lpCursor);
}	
void setcolor(int fg,int bg)
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, bg*16+fg);
}
void draw_bullet(int x, int y)
{
	COORD c = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE) , c);
	printf("   *  ");
}
void erase_bullet(int x, int y)
{
	COORD c = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE) , c);
	printf("      ");
}
int main(){	
	char ch=' ';
	int x=40 ,y=15, checker = 0, i = 0, n = 0;
	int bullet_array[10] = { 999, 999, 999, 999, 999, 999, 999, 999, 999, 999 };
	setcolor(4,2);
	draw_ship(x,y);
	setcursor(0);
	do {

		if (i == 5)
		{
			i = 0;
		}
		if (n == 5)
		{
			n = 0;
		}
		while (n < 5)
		{
			if( bullet_array[(n*2)+1] <= 0 )
			{
				setcolor(0,0);
				erase_bullet(bullet_array[(n*2)], bullet_array[(n*2)+1]);
				setcolor(4,0);
				bullet_array[(n*2)] = 999;
				bullet_array[(n*2) + 1] = 999;
			}
			if(bullet_array[(n*2)] != 999 || bullet_array[(n*2) + 1] != 999)
			{
				setcolor(0,0);
				erase_bullet(bullet_array[(n*2)], bullet_array[(n*2) + 1]);
				setcolor(4,0);
				draw_bullet(bullet_array[(n*2)], --bullet_array[(n*2) + 1]);
			}
			n++;
		}
		if (checker == 4)
		{
			setcolor(0,0);
			erase_ship(x, y);
			setcolor(4,2);
			draw_ship(--x,y);
		}
		if (checker == 6)
		{
			setcolor(0,0);
			erase_ship(x, y);
			setcolor(4,2);
			draw_ship(++x,y);
		}
		//margin out marjin
		if(x <= 0 || x >= 80 || y <= 0 || y >= 80)
		{
			checker = 0;
		}
		
		if (_kbhit()){
			ch=_getch();
			
			/*if(ch=='a' && x > 0) 
			{
				setcolor(0,0);
				erase_ship(x,y);
				setcolor(4,2);
				draw_ship(--x,y);
				sleep(1);
			}
			if(ch=='d' && x < 73) 
			{	
				setcolor(0,0);
				erase_ship(x,y);
				setcolor(4,2);
				draw_ship(++x,y);
				sleep(1);
			}
			if(ch=='w' && y > 0) 
			{
				setcolor(0,0);
				erase_ship(x,y);
				setcolor(4,2);
				draw_ship(x,--y);
			}	
			if(ch=='s' && y <= 20) 
			{
				setcolor(0,0);
				erase_ship(x,y);
				setcolor(4,2);
				draw_ship(x,++y);	
			}*/
			//tap checker 
			// stop when push 's' or touch marjin
			if(ch == 's' || x >= 80 || x <= 0 || y >= 80 || y <= 0)
			{
				checker = 0;
			}		
			// move left // add x > 0
			if(ch =='a' && checker == 0 && x > 0)
			{
				checker = 4;
			}
			// move right
			if(ch =='d' && checker == 0 && x < 80)
			{
				checker = 6;
			}
			
			// firer !!
			if(ch == ' ' && bullet_array[(i * 2)] == 999 && bullet_array[(i * 2) + 1] == 999)
			{
				bullet_array[(i * 2)] = x;
				bullet_array[(i * 2) + 1] = y - 1;
				i++ ;
			}
			fflush(stdin);
		}
		 Sleep(1);	
	}
	while (ch!='x');
	return (0);
}

