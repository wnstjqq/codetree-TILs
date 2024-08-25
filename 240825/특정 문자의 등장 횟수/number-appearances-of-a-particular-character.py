string = input()

ee_cnt, eb_cnt = 0, 0

for i in range(len(string) - 2 + 1):
    if string[i:i+2] == "ee":
        ee_cnt += 1
    if string[i:i+2] == "eb":
        eb_cnt += 1

print(ee_cnt, eb_cnt)