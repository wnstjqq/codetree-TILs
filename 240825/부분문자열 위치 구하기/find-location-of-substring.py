s = input()
p = input()

index = -1

for i in range(len(s) - len(p) + 1):
    for j in range(len(p)):
        if s[i:i+len(p)] == p:
            index = s.index(p[0])

print(index)