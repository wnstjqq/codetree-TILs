N = int(input())

def div_by_10(N):
    s = 0
    for i in range(1, N+1):
        s += i
    return s // 10

print(div_by_10(N))