s = input()

print(s)

for _ in range(len(s)):
    print(s[-1] + s[:-1])
    s = s[-1] + s[:-1]