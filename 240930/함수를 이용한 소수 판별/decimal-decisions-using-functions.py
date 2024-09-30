a, b = map(int, input().split())

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

s = 0 

for j in range(a, b + 1):
    if a == 1:
        break
    if isPrime(j):
        s += j

print(s)