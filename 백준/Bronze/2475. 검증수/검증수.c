#include<stdio.h>
#pragma warning (disable:4996)
int main() {
	int a[5];
	int cnt = 0;

	for (int i = 0; i < 5; i++)
	{	
		scanf(" %d", &a[i]);
		cnt += (a[i] * a[i]);
	}
	cnt %= 10;
	printf("%d", cnt);
}