a,b = map(int, input().split())

remainder = [0] * b

while a > 1:
    remainder[a % b] += 1
    a = a // b

print(sum([i ** 2 for i in remainder]))