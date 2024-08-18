arr = []

for _ in range(3):
    inp = input()
    arr.append(len(inp))

print(max(arr) - min(arr))