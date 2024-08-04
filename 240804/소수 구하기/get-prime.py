n = int(input())

for i in range(2, n+1):
    is_prime = True

    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False

    if is_prime == True:
        print(i, end=" ")