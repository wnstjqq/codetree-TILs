arr = []

inp1 = input()
inp2 = input()

for elem1 in inp1:
    arr.append(elem1)

for elem2 in inp2:
    arr.append(elem2)

for i in range(len(arr)):
    if arr[i] == " ":
        arr[i] = ""

for elem in arr:
    print(elem, end="")