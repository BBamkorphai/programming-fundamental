# include <stdio.h>
int main()
{
	int i;
	char str[101];
	fgets(str, 101, stdin);
	for ( i=0 ; i< strlen(str) ; i++)
	{
		if ( str[i] == 'a')
		{
			str[i+1] = '_';
			str[i+2] = '_';
		}
		if ( str[i] == 'e')
		{
			str[i+1] = '_';
			str[i+2] = '_';
		}
		if ( str[i] == 'i')
		{
			str[i+1] = '_';
			str[i+2] = '_';
		}
		if ( str[i] == 'o')
		{
			str[i+1] = '_';
			str[i+2] = '_';
		}
		if ( str[i] == 'u')
		{
			str[i+1] = '_';
			str[i+2] = '_';
		}
		if ( str[i] == '_')
		{
			continue ;
		}
		printf("%c", str[i]);
	}
}
