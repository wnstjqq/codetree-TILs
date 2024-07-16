multiple = True
for _ in range(5):
    a = int(input())
    if a % 3 == 0:
        multiple = False

print(int(multiple))