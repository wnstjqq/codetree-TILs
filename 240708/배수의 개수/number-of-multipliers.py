cnt_three = 0
cnt_five = 0

for _ in range(10):
    a = int(input())
    if a % 3 == 0 or a % 5 == 0:
        if a % 3 != 0:
            cnt_five += 1
        elif a % 5 != 0:
            cnt_three += 1
        else:
            cnt_five += 1
            cnt_three += 1
print(f"{cnt_three} {cnt_five}")