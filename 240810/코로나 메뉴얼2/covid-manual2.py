A, B, C, D = 0, 0, 0, 0

emergency = ""

for _ in range(3):
    arr = input().split()

    cold, temperature = arr[0], int(arr[1])

    if cold == "Y":
        if temperature >= 37:
            A += 1
        else:
            C += 1
    else:
        if temperature >= 37:
            B += 1
        else:
            D += 1

if A >= 2:
    emergency = "E"

print(A, B, C, D, emergency)