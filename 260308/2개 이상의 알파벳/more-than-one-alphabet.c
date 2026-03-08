#include <stdio.h>

char A[101];

int variousAlphabet(char* arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        char c = *(arr + i);
        for (int j = i + 1; j < n; j++) {
            if (c != *(arr + j)) {
                return 1;
            }
        }
    }
    return 0;
}

int lengthArr(char* arr) {
    int length = 0;
    int i = 0;
    while (*(arr + i) != '\0') {
        length++;
        i++;
    }
    return length;
}

int main() {
    scanf("%s", A);
    int n = lengthArr(A);

    if (variousAlphabet(A, n)) {
        printf("Yes");
    } else {
        printf("No");
    }
    
    return 0;
}