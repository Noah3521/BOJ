#include <stdio.h>

int main(void)
{
    int N = 0;
    scanf("%d", &N);
    for(int j = 1; j <= 9; j++)
{
printf("%d * %d = %d\n", N, j, N*j);
}

    return 0;
}