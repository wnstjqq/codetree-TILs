n = int(input())
arr = list(map(int, input().split()))

cnt = [0] * 9

for elem in arr:
    cnt[elem - 1] += 1

for count in cnt:
    print(count)