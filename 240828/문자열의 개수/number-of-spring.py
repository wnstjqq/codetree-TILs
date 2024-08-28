arr = []

while True:
    A = input()
    
    if A == "0":
        break

    arr.append(A)

print(len(arr))

for i in range(0, len(arr) + 1, 2):
    print(arr[i])