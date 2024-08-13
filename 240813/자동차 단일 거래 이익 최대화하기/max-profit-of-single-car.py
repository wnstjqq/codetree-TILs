n = int(input())
arr = list(map(int, input().split()))

buy = min(arr)
arr.remove(buy)
arr = arr[buy:]

if buy > max(arr):
    print(0)
else:
    print(max(arr) - buy)