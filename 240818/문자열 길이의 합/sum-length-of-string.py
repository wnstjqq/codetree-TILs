n = int(input())

inp = [
    input()
    for _ in range(n)
]

s_sting = 0
cnt = 0

for string in inp:
    s_sting += len(string)
    if 'a' in inp:
        cnt += 1

print(s_string, cnt)