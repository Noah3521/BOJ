#include <stdio.h>

int fack(int n)
{
	if (n == 0) 
		return 1;
	return n * fack(n - 1);
}

int main(void)
{
	int n = 0;
	scanf("%d", &n);
	printf("%d", fack(n));
	return 0;
}