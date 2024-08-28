n1, n2 = map(int, input().split())

n = n1 + n2
n = str(n)

cnt = 0

for elem in n:
    if elem == "1":
        cnt += 1

print(cnt)