a = input().split()
b = input().split()

print(int((int(a[0]) >= 19 and a[1] == "M") or (int(b[0]) >= 19 and b[1] == "M")))