A, B = input().split()

s = 0
n1 = ""
n2 = ""

for elem1 in A:
    if elem1.isdigit():
        n1 += elem1
    else:
        break
s += int(n1)
    
for elem2 in B:   
    if elem2.isdigit():
        n2 += elem2
    else:
        break
s += int(n2)

print(s)