while True:
    h, v, s = map(str, input().split())
    h, v = int(h), int(v)
    print(h * v)
    if s == "C":
        break