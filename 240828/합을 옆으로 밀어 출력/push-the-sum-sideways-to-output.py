n = int(input())

s = 0

for _ in range(n):
    num = int(input())
    s += num

s = str(s)

print(s[1:] + s[0])