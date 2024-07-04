a,b = map(int, input().split())

print(f"{a//b}.", end='')

for _ in range(20):
    a = 10 * (a % b)
    print(a // b, end='')