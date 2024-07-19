n = int(input())

for i in range(2 * n):
    if i % 2 == 0:
        for _ in range(1 + i//2):
            print("*", end=" ")
    else:
        for _ in range(int(-0.5 * i + 4.5) + 1):
            print("*", end=" ")
    print()