n = int(input())

for _ in range(n):
    a = int(input())
    cnt = 0
    while a != 1:
        if a % 2 == 0:
            a //= 2
            cnt += 1
        else:
            a = 3 * a + 1
            cnt += 1
    print(cnt)