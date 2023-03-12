#include<stdio.h>
#pragma warning (disable:4996)
int main() {
	int a[8];
	int cnt = 0;

	for (int i = 0; i < 8; i++) {
		scanf(" %d", &a[i]);
	}

	for (int i = 0; i < 7; i++) {
		if (a[i] < a[i + 1]) {
			cnt++;
		}
		else {
			cnt--;
		}
	}

	if (cnt == 7) {
		printf("ascending");
	}
	else if (cnt == -7) {
		printf("descending");
	}
	else {
		printf("mixed");
	}
}