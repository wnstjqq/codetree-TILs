n = int(input())

for _ in range(n):
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])

    s = 0
    for i in range(a, b+1):
        if i % 2 == 0:
            s += i
    
    print(s)