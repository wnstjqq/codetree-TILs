a,b,c = map(int, input().split())

if a < b or a < c:
    if b < c:
        print(c)
    else:
        print(b)
else:
    print(a)