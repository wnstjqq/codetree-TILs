n = int(input())

cnt = 0
for i in range(1,8):
    n //= i
    cnt += 1
    if n <= 1:
        print(cnt)
        break