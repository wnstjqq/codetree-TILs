N = int(input())

cnt = 'A'
for i in range(N):
    for j in range(N):
        if j < i:
            print(" ", end=" ")
        else:
            print(cnt, end=" ")
            cnt = chr(ord(cnt) + 1)
        if ord(cnt) == ord('Z') + 1:
            cnt = 'A'
    print()