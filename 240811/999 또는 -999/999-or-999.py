arr = list(map(int, input().split()))

max_val, min_val = arr[0], arr[0] 

for elem in arr[1:]:
    if elem == -999 or elem == 999:
        break
        
    if max_val < elem:
        max_val = elem

    if min_val > elem:
        min_val = elem
    
print(max_val, min_val)