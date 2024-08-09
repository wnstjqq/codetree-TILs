arr = list(map(int, input().split()))

cnt = [0] * 9

for elem in arr:
    if elem == 0:
        break
    if elem >= 10:
        cnt[elem // 10 - 1] += 1

for i in range(1, 10):
    print(i, "-", cnt[i-1])