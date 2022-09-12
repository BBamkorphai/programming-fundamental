#include <stdio.h>
#include <string.h>
#include <math.h>
int main()
{
    int n, a, b, i;
    scanf("%d", &n);
    for (i=0 ; i<n ; i++)
    {
        scanf("%d %d", &a, &b);
        printf("%d\n", (int)((abs(b-a))/10) + (int)(ceil(((abs(b-a))%10)/10.0)));
    }

    return 0;
}
