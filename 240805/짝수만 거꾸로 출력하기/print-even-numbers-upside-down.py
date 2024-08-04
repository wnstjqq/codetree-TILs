n = int(input())
arr = list(map(int, input().split()))

even_list = []

for elem in arr:
    if elem % 2 == 0:
        even_list.append(elem)

for even_elem in even_list[::-1]:
    print(even_elem, end=" ")