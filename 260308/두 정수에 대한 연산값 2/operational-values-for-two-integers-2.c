#include <stdio.h>

int a, b;

void modifyValue(int* a, int* b) {
    if (*a < *b) {
        *a += 10;
        *b *= 2;
    } else {
        *a *= 2;
        *b += 10;
    }
}

int main() {
    scanf("%d %d", &a, &b);
    
    modifyValue(&a, &b);

    printf("%d %d", a, b);
    
    return 0;
}