#include<stdio.h>
#pragma warning(disable:4996)
#define SIZE 14
int main()
{
	int apt[SIZE + 1][SIZE] = { 0 };  
	for (int i = 0; i < SIZE; i++)
		apt[0][i] = i + 1;
	for (int i = 1; i < SIZE + 1; i++)
		for (int j = 0; j < SIZE; j++) {
			//apt [i][j] = num 값 구하기
			int num = 0;
			for (int k = 0; k <= j; k++)
				num += apt[i - 1][k];
			apt[i][j] = num;
		}
	int i, j, r;
	scanf("%d", &r);
	for (int p = 0; p < r; p++){
		scanf("%d %d", &i, &j);
		printf("%d\n", apt[i][j-1]);
	}
}