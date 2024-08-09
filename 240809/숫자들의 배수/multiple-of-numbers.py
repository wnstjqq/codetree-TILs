n = int(input())
cnt = 0
arr = []

while cnt < 2:
    for i in range(1, 11):
        arr.append(n * i)
        if (n * i) % 5  == 0:
            cnt += 1

for elem in arr:
    print(elem, end=" ")