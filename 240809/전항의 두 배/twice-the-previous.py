a1, a2 = map(int, input().split())
arr = [a1, a2]

for i in range(8):
    arr.append(2 * arr[i] + arr[i + 1])

for elem in arr:
    print(elem, end=" ")