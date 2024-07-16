arr = input().split()
a,b = int(arr[0]), int(arr[1])

cd = False

for i in range(a,b+1):
    if 960 % i == 0 :
        cd = True

print(int(cd))