A = input()

for elem in A:
    if "a" <= elem <= "z":
        print(elem.upper(), end="")
    else:
        print(elem.lower(), end="")