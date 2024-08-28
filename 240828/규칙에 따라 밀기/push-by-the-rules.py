A = input()
direction = input()

for di in direction:
    if di == "L":
        A = A[1:] + A[0]
    
    else:
        A = A[-1] + A[:-1]

print(A)