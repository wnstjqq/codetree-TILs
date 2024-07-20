n = int(input())

if n == 1:
    print("*")

if n % 2 == 0:
    for i in range(n):
        if i == 0:
            for j in range(n):
                print("*", end=" ")
        elif i == 1:
            for j in range(n // 2):
                print(" ", end=" ")
                print("*", end=" ")
        else:
            for j in range(n-1):
                print(" ", end=" ")
            print("*")
else:
    for i in range(n-1):
        if i == 0:
            for j in range(n):
                print("*", end=" ")
        elif i == 1:
            for j in range(int(n // 2)):
                print(" ", end=" ")
                print("*", end=" ")
            print(" ")
        else:
            for j in range(n-2):
                print(" ", end=" ")
            print("*", end=" ")
            print(" ")