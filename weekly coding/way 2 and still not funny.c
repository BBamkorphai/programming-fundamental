#include <stdio.h>

// swap and anragenent
void minimum(int num[], int length)
{
    int count = 1, n = 0 , min ;
    while (count != length + 1)
    {
        min = 10;
        for (int i = 0; i < length; i++)
        {
            if (count == 1 && num[i] == 0)
            {
                continue;
            }
            if (num[i] <= min)
            {
                min = num[i];
                n = i;
            }
        }
        printf("%d",min);
        num[n]= 10;
        count++;
    }
}

// function for input number
void input_num()
{
    int length;
    scanf("%d", &length);
    int num[length];
    for (int i = 0; i < length; i++)
    {
        scanf("%d", &num[i]);
    }
    minimum(num, length);
}

// main so cool
int main()
{
    input_num();
}

