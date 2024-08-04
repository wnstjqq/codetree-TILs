arr = list(map(int, input().split()))

s = 0
cnt = 0

for elem in arr:
    if elem == 0:
        break
    elif elem % 2 == 0:
        s += elem
        cnt += 1

print(cnt, s)