a,b,c = map(int, input().split())
min_num = a
if min_num > min(b,c):
    min_num = min(b,c)
    
print(int(a == min_num), end=' ')
print(int(a==b==c))