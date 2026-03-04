#include <stdio.h>

char A[101];

int isPalindrome(char* string) {
    char* left = string;
    char* right = string;

    while (*right != '\0') {
        right++;
    }
    right--;

    while (left < right) {
        if (*left != *right) {
            return 0;
        }
        left++;
        right--;
    }

    return 1;
}

int main() {
    scanf("%s", A);

    if (isPalindrome(A)) {
        printf("Yes");
    } else {
        printf("No");
    }

    return 0;
}