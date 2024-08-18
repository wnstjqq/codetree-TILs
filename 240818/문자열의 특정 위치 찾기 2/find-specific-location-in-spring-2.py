arr = ["apple", "banana", "grape", "blueberry", "orange"]
ans = []

cnt = 0

inp = input()

for elem in arr:
    if inp in elem[2] or inp in elem[3]:
        ans.append(elem)
        cnt += 1

for elem in ans:
    print(elem)

print(cnt)