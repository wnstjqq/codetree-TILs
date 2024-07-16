n = int(input())

composite = False

for i in range(2,n):
    if n % i == 0:
        composite = True

if composite == True:
    print("C")
else:
    print("N")