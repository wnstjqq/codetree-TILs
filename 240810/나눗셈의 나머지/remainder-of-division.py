a,b = map(int, input().split())

remainder = [0] * b

while a > 1:
    a, b = a // b, b
    remainder[a % b] += 1

print(sum([i ** 2 for i in remainder]))