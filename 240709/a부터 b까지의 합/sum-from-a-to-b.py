inp = input().split()
a, b = int(inp[0]), int(inp[1])

sum_val = 0
for i in range(a,b + 1):
    sum_val += i
print(sum_val)