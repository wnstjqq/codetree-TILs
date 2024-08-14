upper = "A B C D E F G H I J K L M N O".split()
cnt = 0
for _ in range(5):
    arr = input().split()
    for _ in range(len(arr)):
        print(upper[cnt], end=" ")
        cnt += 1
    print()