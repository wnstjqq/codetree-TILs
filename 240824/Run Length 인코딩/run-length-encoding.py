inp = input()

alp = inp[0]
s = [inp[0]]
cnt = 1

for elem in inp[1:]:
    if alp == elem:
        cnt += 1
    else:
        for count in str(cnt):
            s.append(count)
        cnt = 1
        alp = elem
        s.append(alp)
s.append(cnt)

print(len(s))

for elem in s:
    print(elem, end="")