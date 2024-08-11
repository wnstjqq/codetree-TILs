N = int(input())

arr = list(map(int, input().split()))

max_val = arr[0]

for elem1 in arr[1:]:
    if max_val < elem1:
        max_val = elem1

if arr.count(max_val) >= 2:
    print(max_val, max_val)

else:
    max_val = arr[0]
    second_max_val = arr[0]

    for elem2 in arr[1:]:
        if max_val < elem2:
            max_val = elem2
    
    if max_val == arr[0]:
        second_max_val = arr[1]

    arr.remove(max_val)
    for elem3 in arr[1:]:
        if second_max_val < elem3:
            second_max_val = elem3
            
    print(max_val, second_max_val)