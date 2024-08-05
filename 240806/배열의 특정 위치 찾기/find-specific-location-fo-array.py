arr = list(map(int, input().split()))

s_even = 0
s_odd = 0
cnt_odd = 0

for i in range(len(arr)):
    if (i+1) % 2 == 0:
        s_even += arr[i]
    elif (i+1) % 3 == 0:
        s_odd += arr[i]
        cnt_odd += 1

print(f"{s_even} {s_odd / cnt_odd:.1f}")