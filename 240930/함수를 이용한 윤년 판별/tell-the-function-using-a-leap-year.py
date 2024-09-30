y = int(input())

def leap(y):
    if y % 4 != 0:
        return False
    if y % 100 == 0 and y % 400 != 0:
        return False
    return True

if leap(y):
    print("true")
else:
    print("false")