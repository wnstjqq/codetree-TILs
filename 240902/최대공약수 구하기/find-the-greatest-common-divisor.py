n, m = map(int, input().split())

def gcd(n, m):
    gcd = 1
    for i in range(2, min(n,m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
    print(gcd)

gcd(n, m)