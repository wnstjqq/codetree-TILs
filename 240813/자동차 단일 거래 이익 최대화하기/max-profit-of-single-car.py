n = int(input())
arr = list(map(int, input().split()))

max_numbers = []

if len(arr) == 1:
    print(0)
    
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        profit = []
        if arr[i] < arr[j]:
            profit.append(arr[j] - arr[i])
            max_numbers.append(max(profit))

print(max(max_numbers))