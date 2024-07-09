n = int(input())

sum_val, cnt = 0, 0

for _ in range(n):
    a = int(input())
    sum_val += a
    cnt += 1

print(f"{sum_val} {sum_val/cnt:.1f}")