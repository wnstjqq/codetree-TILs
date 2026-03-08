#include <stdio.h>

void modifyInteger(int* a, int* b) {
    if (*a < *b) {
        *a *= 2;
        *b += 25;
    } else {
        *a += 25;
        *b *= 2;
    }
}

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);

    modifyInteger(&a, &b);

    printf("%d %d", a, b);

    return 0;
}