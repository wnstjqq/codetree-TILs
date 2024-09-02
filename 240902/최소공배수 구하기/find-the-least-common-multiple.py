n, m = map(int, input().split())

def lcm(n, m):
    result = 1
    for i in range(2, min(n,m) + 1):
        if n % i == 0 and m % i == 0:
            result *= i
            n //= i
            m //= i
            continue
    result *= n * m
    print(result)

lcm(n, m)