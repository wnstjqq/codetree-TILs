a,b = map(int, input().split())

prod = a
for _ in range(b):
    prod *= a

print(prod)