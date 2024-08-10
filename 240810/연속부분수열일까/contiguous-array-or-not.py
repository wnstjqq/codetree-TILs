n1, n2 = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

if arr2[0] not in arr1:
    print("No")

for _ in range(arr1.count(arr2[0])):
    main_list, sub_list = [], []
    
    idx = arr1.index(arr2[0])
    
    for i in range(len(arr2)):
        main_list.append(arr1[idx])
        sub_list.append(arr2[i])
        
        idx += 1

    if main_list == sub_list:
        print("Yes")
        break
    else:
        arr1.remove(arr2[0])

if arr1.count(arr2[0]) == 0:
    print("No")