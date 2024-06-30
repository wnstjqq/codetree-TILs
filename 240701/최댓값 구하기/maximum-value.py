a,b,c = map(int, input().split())

max_num = a
if max_num < b:
    if b < c:
        print(c)
    else:
        max_num = b
        print(max_num)
else:
    print(max_num)