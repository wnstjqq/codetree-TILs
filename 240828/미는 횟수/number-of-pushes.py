A = input()
B = input()

cnt = 0

for _ in range(len(A) + 1):
    if A == B: break

    A = A[-1] + A[:-1]
    cnt += 1

if cnt == len(A) + 1:
    print(-1)
else:
    print(cnt)