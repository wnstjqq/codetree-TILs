inp = input()
n = int(input())

if n > len(inp):
    print(inp[::-1])
else:
    for i in range(n):
        print(inp[::-1][i], end="")