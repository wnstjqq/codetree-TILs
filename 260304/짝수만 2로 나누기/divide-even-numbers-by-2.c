#include <stdio.h>

int n;
int arr[50];

int* dividedByTwo(int* arr, int n) {
    for (int i = 0; i < n; i++) {
        if (*(arr + i) % 2 == 0) {
            *(arr + i) /= 2;
        }
    }
    return arr;
}

void printElements(int* arr, int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", *(arr + i));
    }
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    dividedByTwo(arr, n);

    printElements(arr, n);

    return 0;
}