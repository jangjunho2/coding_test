#include<stdio.h>

int main(){

	int R;
	scanf("%d", &R);
	for (int i = 0; i < R; i++) {
		int a, b, res;
		scanf("%d %d", &a, &b);
		res = a;
		for (int j = 1; j < b; j++) {
			res *= a;
			res %= 10;
		}

		if (res > 10) {
			res %= 10;
		}

		if (res == 0) {
			printf("10\n");
			continue;
		}
		printf("%d\n", res);
	}
}