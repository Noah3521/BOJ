#include <stdio.h>

void hanoi(int n, int from, int mid, int to)
{
	if (n == 1)
	{
		printf("%d %d\n", from, to);
		return;
	}
	hanoi(n - 1, from, to, mid);
	printf("%d %d\n",from, to);
	hanoi(n - 1, mid, from, to);
}

int pow(int a, int b)
{
	int result = 1;
	for (int i = 1; i <= b; i++)
	{
		result *= a;
	}
	return result -1 ;
}

int main(void)
{
	int n = 0;
	scanf("%d", &n);
	printf("%d\n", pow(2, n));
	hanoi(n, 1, 2, 3);

	return 0;
}