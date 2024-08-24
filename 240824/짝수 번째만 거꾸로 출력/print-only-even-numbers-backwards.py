inp = input()

s = ""

for elem in inp[1::2]:
    s += elem

print(s[::-1])