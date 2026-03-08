#include <stdio.h>
#define MAX_N 50

int arr[MAX_N];

void absoluteValue(int* arr, int n) {
    for (int i = 0; i < n; i++) {
        if (*(arr + i) < 0) {
            *(arr + i) *= -1;
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    absoluteValue(arr, n);

    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    
    return 0;
}