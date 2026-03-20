#include <stdio.h>

int arr[101];
int cnt;

int addElement(int n, int cnt) {
    int sum = 0;

    while (cnt != 0) {
        if (cnt % 2 == 0) {
            sum += arr[cnt];
            cnt /= 2;
        } else {
            sum += arr[cnt];
            cnt--;
        }
    }
    return sum;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++)
        scanf("%d", &arr[i]);
    cnt = m;
    
    printf("%d", addElement(n, cnt));
    
    return 0;
}