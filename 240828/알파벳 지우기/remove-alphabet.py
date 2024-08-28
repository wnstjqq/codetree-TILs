A = input()
B = input()

a = ""
b = ""

for elem1 in A:
    if elem1.isdigit():
        a += elem1

for elem2 in B:
    if elem2.isdigit():
        b += elem2

print(int(a) + int(b))