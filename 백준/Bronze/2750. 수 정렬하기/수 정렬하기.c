#include<stdio.h>
#include<stdlib.h>
#pragma warning (disable:4996)

void ins_sort(int arr[], int size) {
	for (int i = 0; i < size - 1; i++) {

		if (arr[i] <= arr[i + 1]) {
			continue;
		}

		else {
			for (int j = i; 0 <= j; j--) {
				if (arr[j] > arr[j + 1]) {
					int temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
				}
				else {
					break;
				}

			}
		}
	}
}

int main()
{
	//삽입 정렬
	int size;
	scanf(" %d", &size);

	int* arr = (int*)malloc(sizeof(int) * size);

	for (int i = 0; i < size; i++) {
		scanf(" %d", &arr[i]);
	}


	ins_sort(arr, size);

	for (int i = 0; i < size; i++) {
		printf("%d\n", arr[i]);
	}

}