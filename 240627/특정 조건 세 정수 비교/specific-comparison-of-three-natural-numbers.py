a,b,c = map(int, input().split())

print(int(a == min(a,b) and a == min(b,c) and a == min(a,c)), end=' ')
print(int(a==b==c))