#include<stdio.h>
#include<windows.h>
void draw_ship(int x,int y)
{
	printf(" <-0-> ");
}
void gotoxy(int x, int y)
{
	COORD c = { x, y };
	SetConsoleCursorPosition(
	GetStdHandle(STD_OUTPUT_HANDLE) , c);
}
int main()
{		
	draw_ship(1,20);
	return 0;
}
