arr = input().split()

for i in range(1, len(arr)):
    if int(arr[i]) >= 250:
        arr = arr[:i]
        break

s = 0
for elem in arr:
    s += int(elem)
print(f"{s} {s/len(arr):.1f}")