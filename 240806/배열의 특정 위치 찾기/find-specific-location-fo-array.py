arr = list(map(int, input().split()))

s_even = 0
s_odd = 0
cnt_odd = 0

for i in range(1, len(arr), 2):
    s_even += arr[i]
for j in range(2, len(arr), 3):
    s_odd += arr[j]
    cnt_odd += 1

print(f"{s_even} {s_odd / cnt_odd:.1f}")