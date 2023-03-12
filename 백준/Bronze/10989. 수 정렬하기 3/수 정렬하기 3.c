#include<stdio.h>
#include<stdlib.h>
#pragma warning(disable:4996)
int main()
{
	int size, temp;
	int cnt[10000] = { 0 };
	scanf("%d", &size);
	for (int i = 0; i < size; i++) {
		scanf("%d", &temp);
		cnt[temp - 1]++;
	}
	for (int i = 0; i < 10000; i++) {  
		for (int j = 0; j < cnt[i]; j++) {
			printf("%d\n", i + 1);
		}
	}
}