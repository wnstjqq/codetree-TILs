n = int(input())

inp = [
    input()
    for _ in range(n)
]

s_string = 0
cnt = 0

for string in inp:
    s_string += len(string)
    if 'a' in string:
        cnt += 1

print(s_string, cnt)