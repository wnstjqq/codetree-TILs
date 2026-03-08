#include <stdio.h>
#include <string.h>

char text[1001];
char pattern[1001];

int isPart(int start_idx, int m) {
    for (int j = 1; j < m; j++) {
        if (text[start_idx + j] != pattern[j]) {
            return 0;
        }
    }
    return 1;
}

int findIdx() {
    int n = strlen(text);
    int m = strlen(pattern);
    
    for (int i = 0; i <= n - m; i++) {
        if (text[i] == pattern[0]) {
            if (isPart(i, m)) {
                return i;
            }
        }
    }
    return -1;
}

int main() {
    scanf("%s", text);
    scanf("%s", pattern);

    printf("%d", findIdx());    
    
    return 0;
}