n = int(input())
1,3,5,7,8,10,12
2,4,6,9,11
if n <= 7:
    if n % 2 == 1:
        print(31)
    else:
        if n == 2:
            print(28)
        else:
            print(30)
else:
    if n % 2 == 0:
        print(31)
    else:
        print(30)