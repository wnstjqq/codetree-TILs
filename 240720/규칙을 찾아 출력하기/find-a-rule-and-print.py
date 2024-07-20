n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == 5 or j == 0 or j == 5:
            print("*", end=" ")
        else:
            if i >= j+1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()