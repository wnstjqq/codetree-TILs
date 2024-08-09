arr = list(map(int, input().split()))

cnt = [0] * 6

for elem in arr:
    cnt[elem - 1] += 1

for i in range(1, 7):
    print(i, "-", cnt[i - 1])