str = input()

str = list(str)

f, s = str[0], str[1]
for i in range(len(str)):
    if str[i] == f:
        str[i] = s
    elif str[i] == s:
        str[i] = f

print("".join(str))