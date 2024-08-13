n = int(input())
arr = list(map(int, input().split()))

_min = []

for i in range(n):
    for j in range(i + 1, n):
        sub = arr[j] - arr[i]
        _min.append(sub)

print(min(_min))