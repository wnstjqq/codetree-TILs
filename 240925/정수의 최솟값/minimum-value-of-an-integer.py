a, b, c = map(int, input().split())

def minimum(a, b, c):
    return min(min(a,b), c)

print(minimum(a, b, c))