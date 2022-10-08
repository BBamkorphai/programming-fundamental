#include <stdio.h>
#include <windows.h>
#include <conio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
//#include <thread>

void setcolor(int fg,int bg)
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, bg*16+fg);
}
void draw_ship (short x,short y)
{
	COORD c = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE) , c);
	setcolor(4,2);
	printf(" <-0-> ");
}
void erase_ship(short x,short y)
{
	COORD c = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE) , c);
	printf("       ");
}
char cursor(short x, short y)
{
	HANDLE hStd = GetStdHandle(STD_OUTPUT_HANDLE);
	char buf[2]; COORD c = {x,y}; DWORD num_read;
	if(!ReadConsoleOutputCharacter(hStd,(LPTSTR)buf,1,c,(LPDWORD)&num_read) )
	return '\0';
	else
	return buf[0];
}
void setcursor(int visible)
{
	HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
	CONSOLE_CURSOR_INFO lpCursor;
	lpCursor.bVisible = visible;
	lpCursor.dwSize = 20;
	SetConsoleCursorInfo(console,&lpCursor);
}	
void draw_bullet(short x, short y)
{
	COORD c = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE) , c);
	printf("|");
}
void erase_bullet(short x, short y)
{
	setcolor(2, 0);
	COORD c = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE) , c);
	printf(" ");
}
void    draw_star(short x, short y)
{
    setcolor(7, 0);
    COORD c = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE) , c);
    printf("*");
}
void    show_score(short x, short y, int score)
{
    COORD c = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE) , c);
    printf("score: %d", score);
}
int main(){	
	char ch=' ';
	int x=40 ,y=15, checker = 0, i = 0, n = 0, j = 0, star_X_line, star_Y_line, score = 0;
	int bullet_array[10] = { 999, 999, 999, 999, 999, 999, 999, 999, 999, 999 };
	srand(time(NULL));
	setcursor(0);
	draw_ship(x,y);
	
	// random star
	while (j < 8)
    {
        star_X_line = 10 + (rand() % 61);
        star_Y_line = 2 + (rand() % 4);
        if(cursor(star_X_line, star_Y_line) != '*')
        {
            draw_star(star_X_line, star_Y_line);
            j++;
        }
        else
            j = j;
    }
	
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
			if(bullet_array[(n * 2)] != 999 || bullet_array[(n * 2) + 1] != 999)
            {
                erase_bullet(bullet_array[(n * 2)], bullet_array[(n * 2) + 1]);
                if(cursor(bullet_array[(n * 2)], bullet_array[(n * 2) + 1] - 1) == '*')
                // engaged star
                {
                	score += 1000;
                	show_score(2, 21, score);
                    erase_bullet(bullet_array[(n * 2)], bullet_array[(n * 2) + 1] - 1);
                    do
                    {        
                        star_X_line = 10 + (rand() % 61);
                        star_Y_line = 2 + (rand() % 4);
                    } while (cursor(star_X_line, star_Y_line) == '*');
                    draw_star(star_X_line, star_Y_line);
                    bullet_array[(n * 2)] = 999;
                    bullet_array[(n * 2) + 1] = 999;
                }
                else
                {
                    draw_bullet(bullet_array[(n * 2)], --bullet_array[(n * 2) + 1]);
                }
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
				bullet_array[(i * 2)] = x + 3;
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


