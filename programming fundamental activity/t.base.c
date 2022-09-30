#include <thread>
#include <mutex>
#include <windows.h>
#include <time.h>
#define bound_x 80
#define bound_y 18
int nowstar = 0;
std::mutex mtx;
void gotoxy(int x, int y)
{
 COORD c = { x, y };
 SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
}
char cursor(int x, int y) {
 HANDLE hStd = GetStdHandle(STD_OUTPUT_HANDLE);
 char buf[2]; COORD c = { x,y }; DWORD num_read;
 if (!ReadConsoleOutputCharacter(hStd, (LPTSTR)buf, 1, c, (LPDWORD)& num_read))
 return '\0';
 else
 return buf[0];
}
void setcursor(bool visible)
{
 HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
 CONSOLE_CURSOR_INFO lpCursor;
 lpCursor.bVisible = visible;
 lpCursor.dwSize = 20;
 SetConsoleCursorInfo(console, &lpCursor);
}
int ball(int x, int y)
{
 int stpx, stpy;
 bool col;
 nowstar += 1;
 stpx = 1 - (2 * (x % 2));
 stpy = 1 - (2 * (y % 2));
 col = false;
 while (!col) 
 {
 if ((cursor(x-1,y) == '*') || (cursor(x+1,y) == '*' ) || (x <= 2) || (x >= bound_x-2)) {
 stpx = -stpx;
 //std::thread q(Beep, 700, 500);
 //q.detach();
 }
 if ((cursor(x, y-1) == '*') || (cursor(x , y+1) == '*') || (y <= 2) || (y >= bound_y-2)) {
 stpy = -stpy;
 //std::thread q(Beep, 700, 500);
 //q.detach();
 }
 mtx.lock();
 gotoxy(x, y);
 printf(" ");
 mtx.unlock();
 x = x + stpx;
 y = y + stpy;
 if (cursor(x, y) == '#') {
 nowstar -= 1;
 col=true;
 } 
 else {
 mtx.lock();
 gotoxy(x, y);
 printf("*");
 mtx.unlock();
 }
 Sleep(100);
 }
 return 0;
}
int main()
{
 srand(time(NULL));
 setcursor(0);
 gotoxy(25, 10);
 printf("##");
 for (int i = 0; i < 20; i++)
 {
 std::thread q(ball,rand() % 10 + 35,rand() % 10 + 5);
 q.detach();
 }
 do {
 mtx.lock();
 gotoxy(50, 10);
 printf("  %d  ", nowstar);
 mtx.unlock();
 Sleep(1000);
 } while (nowstar > 0);
 return 0;
}
