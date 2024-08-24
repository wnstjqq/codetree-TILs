inp = input()

alp = inp[0]
s = ""
s += alp
cnt = 1

for elem in inp[1:]:
    if alp == elem:
        cnt += 1
    else:
        s += str(cnt)
        cnt = 1
        alp = elem
        s += alp
s += str(cnt)

print(len(s))
print(s)