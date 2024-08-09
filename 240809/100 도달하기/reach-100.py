n = int(input())

arr = [1, n]

cnt = 0

while True:
    if arr[cnt] + arr[cnt + 1] > 100:
        arr.append(arr[cnt] + arr[cnt + 1])
        break
    arr.append(arr[cnt] + arr[cnt + 1])
    cnt += 1

for elem in arr:
    print(elem, end=" ")