s = input()

a, b = s[0], s[1]

s = list(s)

for i in range(len(s)):
    if s[i] == b:
        s[i] = a

print("".join(s))