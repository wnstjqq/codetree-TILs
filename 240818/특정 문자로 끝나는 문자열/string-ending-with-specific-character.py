inp = [
    input()
    for _ in range(10)
]

alp = input()

cnt = 0

for string in inp:
    if string[-1] == alp:
        cnt += 1
        print(string)

if cnt == 0:
    print("None")