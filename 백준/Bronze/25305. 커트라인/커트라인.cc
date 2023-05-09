/*
첫째줄에 인원수, 등수를 입력하면
커트라인 점수를 출력해주는 프로그램
*/
#include <stdio.h>
#include <stdlib.h>

void selectSort(int* arr, int N)
{
	for (int i = 1; i < N; i++)
	{
		for (int j = 0; j < N - 1; j++)
		{
			if (arr[j] < arr[i])
			{
				int tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
	}
}

int main(void)
{
	int N = 0; // 응시자 수
	int k = 0; // 상을 받는 사람 수
	scanf("%d", &N);	// 응시자 수 입력
	scanf("%d", &k);// 상 받는사람 수 입력
	int* arr = (int*)malloc(sizeof(arr) * N);	// N크기의 배열 선언
	
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &arr[i]);	// 점수 입력
	}
	selectSort(arr, N);
	printf("%d ", arr[k-1]);	// 점수 입력
	
	return 0;
}