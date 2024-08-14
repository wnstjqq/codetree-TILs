arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

print(f"{sum(arr_2d[0]) / 4:.1f} {sum(arr_2d[1]) / 4:.1f}")

for i in range(1):
    for j in range(4):
        print(f"{(arr_2d[i][j] + arr_2d[i+1][j]) / 2:.1f}", end=" ")
    print()

print(f"{(sum(arr_2d[0]) + sum(arr_2d[1])) / 8:.1f}")