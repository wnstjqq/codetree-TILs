N = int(input())
arr = list(map(int, input().split()))

while len(arr) != 0:
    print(arr.index(max(arr)) + 1, end=" ")
    arr = arr[:arr.index(max(arr))]