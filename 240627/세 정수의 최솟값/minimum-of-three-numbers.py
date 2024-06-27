a,b,c = map(int, input().split())

min_num = a
if min_num > min(b,c):
    min_num = min(b,c)
print(min_num)