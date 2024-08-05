arr = list(map(int, input().split()))

s_even = 0
s_odd = 0
cnt_odd = 0

for i in range(1, len(arr) + 1):
    if i % 2 == 0:
        s_even += arr[i-1]
    elif i % 3 == 0:
        s_odd += arr[i-1]
        cnt_odd += 1

print(f"{s_even} {s_odd / cnt_odd:.1f}")