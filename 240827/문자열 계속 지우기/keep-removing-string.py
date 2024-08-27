A = input()
B = input()

cnt = 0

while True:
    lena = len(A)
    lenb = len(B)

    A = "".join(A)
    if A[cnt:cnt+lenb] == B:
        A = list(A)
        for i in range(lenb - 1, -1, -1):
            A.pop(cnt + i)
        cnt = 0
    else:
        cnt += 1
    
    if cnt == lena - lenb + 1:
        break

    if lena == 0:
        break
    
    if lena < lenb:
        break

print("".join(A))