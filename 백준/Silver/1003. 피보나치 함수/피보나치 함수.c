#include<stdio.h>

int main() {
	int R, n;

	scanf("%d", &R);
	for (int i = 0; i < R; i++)
	{
		int t0[2] = { 1,0 };
		int t1[2] = { 0,1 };
		int next[2];

		n = 0;
		scanf("%d", &n);
		for (int j = 0; j < n; j++) {
			next[0] = t0[0] + t1[0];
			t0[0] = t1[0];
			t1[0] = next[0];

			next[1] = t0[1] + t1[1];
			t0[1] = t1[1];
			t1[1] = next[1];
		}
		printf("%d %d\n", t0[0], t0[1]);
	}
}
