arr = list(map(int, input().split()))\

cnt = [0] * 10
grade = [x * 10 for x in range(10, 0, -1)]

for elem in arr:
    if elem == 0:
        break
    cnt[elem // 10 - 1] += 1

for i in range(10):
    print(grade[i], "-", cnt[9-i])