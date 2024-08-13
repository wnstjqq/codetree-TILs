arr = list(map(int, input().split()))

over500, under500 = [], []

for elem in arr:
    if elem > 500:
        over500.append(elem)
    else:
        under500.append(elem)

print(max(under500), min(over500))