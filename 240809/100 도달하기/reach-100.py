n = int(input())

arr = [1, n]

cnt = 0

while True:
    arr.append(arr[cnt] + arr[cnt + 1])
    if arr[cnt + 2] > 100:
        break
    cnt += 1

for elem in arr:
    print(elem, end=" ")