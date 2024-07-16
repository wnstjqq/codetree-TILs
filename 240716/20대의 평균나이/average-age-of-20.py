sum_value = 0
cnt = 0

while True:
    n = int(input())
    if 19 < n < 30:
        sum_value += n
        cnt += 1
    else:
        print(f"{sum_value/cnt:.2f}")