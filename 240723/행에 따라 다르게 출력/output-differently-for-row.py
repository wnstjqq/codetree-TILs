n = int(input())

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            if i == 0:
                print(j+1, end=" ")
            else:
                print(3 * n + j+1, end=" ")
        else:
            if i == 1:
                print(n + 2 * (j+1), end=" ")
            else:
                print(3 * n + n + 2 * (j+1), end=" ")
    print()