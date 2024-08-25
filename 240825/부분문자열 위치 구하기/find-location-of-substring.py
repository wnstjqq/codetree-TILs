s = input()
p = input()

index = -1

for i in range(len(s) - len(p) + 1):
    if s[i:i+len(p)] == p:
        index = i
        break

print(index)