N = input()

def even_ikhim(N):
    return int(N) % 2 == 0 and (int(N[0]) + int(N[1])) % 5 == 0

if even_ikhim(N) == True:
    print("Yes")
else:
    print("No")