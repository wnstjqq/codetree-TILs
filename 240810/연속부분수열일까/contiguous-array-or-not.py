n1, n2 = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for elem1 in arr1:
    if elem1 == arr2[0]:
        idx = arr1.index(arr2[0])

while idx < len(arr2):
    for elem2 in arr2:
        if elem2 != arr1[idx]:
            print("No")
            break
        else:
            idx += 1
    
if idx == arr2.index(arr2[-1]):
    print("Yes")