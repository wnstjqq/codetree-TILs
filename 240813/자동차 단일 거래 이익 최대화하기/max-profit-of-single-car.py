n = int(input())
arr = list(map(int, input().split()))

max_numbers = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        profit = []
        if arr[i] <= arr[j]:
            profit.append(arr[j] - arr[i])
            max_numbers.append(max(profit))

if len(max_numbers) == 0:
    print(0)
else:
    print(max(max_numbers))