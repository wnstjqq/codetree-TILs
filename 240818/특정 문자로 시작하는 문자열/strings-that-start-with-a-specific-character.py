n = int(input())

inp = [
    input()
    for _ in range(n)
]

alp = input()

cnt = 0
s = 0

for string in inp:
    if string[0] == alp:
        cnt += 1
        s += len(string)

print(f"{cnt} {s / cnt:.2f}")