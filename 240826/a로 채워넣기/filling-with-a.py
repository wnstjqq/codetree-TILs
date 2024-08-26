string = input()

string = list(string)

string[1], string[-2] = 'a', 'a'

print("".join(string))