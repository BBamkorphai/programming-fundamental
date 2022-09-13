#include <stdio.h>
#include <string.h>

int main()
{
	char *p,charbox[999];
	p = charbox;
	scanf("%s", charbox);
	while ( *p != '\0')
	{
		if ( *p >= 'a' && *p <= 'z')
		{
			printf("%c", *p-32);
		}
		if ( *p >= 'A' && *p <= 'Z')
		{
			printf("%c", *p+32);
		}
		p++;
	}
	return 0;
}
