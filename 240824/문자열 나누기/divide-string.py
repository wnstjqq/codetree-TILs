n = int(input())

arr = input().split()

arr_2 = "".join(arr)

for i in range(len(arr_2)):
    print(arr_2[i], end="")
    if (i + 1) % 5 == 0:
        print()