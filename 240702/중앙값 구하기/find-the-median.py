a,b,c = map(int, input().split())

if a < b:
    if a > c:
        print(a)
    else:
        if b < c:
            print(b)
        else:
            print(c)
else:
    if b > c:
        print(b)
    else:
        if a < c:
            print(a)
        else:
            print(c)