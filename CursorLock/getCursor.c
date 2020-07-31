#include <stdio.h>
#include <windows.h>

int main()
{
	POINT p;
	while(1){
		Sleep(50); //等待50毫秒 
		GetCursorPos(&p);
		printf("\r                      \r鼠标位置: %d,%d",p.x,p.y);
	}
	return 0;
}
