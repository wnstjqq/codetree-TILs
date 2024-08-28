s = input()

for elem in s:
    if elem.isdigit() or elem.isalpha():
        print(elem.lower(), end="")