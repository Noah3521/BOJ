#include <stdio.h>

int main(void)
{
    int chess[6] = { 1, 1, 2, 2, 2, 8 };
    int result[6] = { 0 };
    for (int i = 0; i < 6; i++)
    {
        scanf("%d", &result[i]);
    }
    for (int i = 0; i < 6; i++)
    {
        printf("%d ", chess[i] - result[i]);
    }
    return 0;
}