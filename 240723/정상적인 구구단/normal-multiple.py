n = int(input())

for i in range(n):
    for j in range(n):
        if j != n-1:
            print(f"{i+1} * {j+1} = {(i+1) * (j+1)}", end=", ")
        else:
            print(f"{i+1} * {j+1} = {(i+1) * (j+1)}", end="")
    print()