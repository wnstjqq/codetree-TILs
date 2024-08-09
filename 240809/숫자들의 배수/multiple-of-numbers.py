n = int(input())

multiple_5 = 0

cnt = 1
while multiple_5 != 2:
    if (cnt * n) % 5 == 0:
        multiple_5 += 1
    print(cnt * n, end=" ")
    cnt += 1