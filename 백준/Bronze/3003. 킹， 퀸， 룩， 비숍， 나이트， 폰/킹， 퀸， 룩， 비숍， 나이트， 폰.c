#include<stdio.h>
#pragma warning (disable:4996)
int main()
{
	int num[6] = { 1,1,2,2,2,8 };
	int ans[6];
	for (int i = 0; i < 6; i++) {
		scanf(" %d", &ans[i]);
	}

	for (int i = 0; i < 6; i++) {
		printf("%d ",num[i]-ans[i]);
	}
}