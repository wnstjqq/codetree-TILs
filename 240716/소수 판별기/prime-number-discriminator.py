n = int(input())

prime = True
for i in range(2,int(n**0.5) + 1):
    if n % i == 0:
        prime = False

if prime == True:
    print("P")
else:
    print("C")