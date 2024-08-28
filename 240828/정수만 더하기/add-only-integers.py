A = input()

s = 0

for elem in A:
    if elem.isdigit():
        s += int(elem)

print(s)