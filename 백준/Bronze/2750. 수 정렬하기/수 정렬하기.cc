/*
	============입력============
	첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 
	둘째 줄부터 N개의 줄에는 수가 주어진다. 
	이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 
	수는 중복되지 않는다.
	============출력============
	첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
*/
#include <stdio.h>

void getArr(int* arr, int max)
{
	for (int i = 0; i < max; i++)	// max개수만큼 arr입력
	{
		scanf("%d", &arr[i]);
	}
}

void printArr(int* arr, int max)
{
	for (int i = 0; i < max; i++)	// max개수만큼 arr출력
	{
		printf("%d\n", arr[i]);
	}
}

void selectSort(int* arr, int max)
{
	int tmp = 0;
	for (int i = 1; i < max; i++)
	{
		for (int j = 0; j < max - 1; j++)
		{
			if (arr[j] > arr[i])
			{
				tmp = arr[j];
				arr[j] = arr[i];
				arr[i] = tmp;
			}
		}
	}
}

int main(void)
{
	int arr[1000] = { 0 };	// 배열 1000개 생성
	int max = 0;	
	scanf("%d", &max);	// 생성할 배열 개수 입력

	getArr(arr, max);	// max개수만큼 arr입력

	selectSort(arr, max);

	printArr(arr, max);	// max개수만큼 arr출력
	


	return 0;
}