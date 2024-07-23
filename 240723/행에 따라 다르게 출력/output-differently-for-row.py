n = int(input())

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(3 * n * i // 2 + j+1, end=" ")
        else:
            print(3 * n * int(i // 2) + n + 2 * (j+1), end=" ")
    print()