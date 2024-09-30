a, b = map(int, input().split())

def multiple_3(n):
    return n % 3 == 0

def tsn(n):
    n = str(n)
    return "3" in n or "6" in n or "9" in n

cnt = 0

for i in range(a, b + 1):
    if multiple_3(i) or tsn(i):
        cnt += 1

print(cnt)