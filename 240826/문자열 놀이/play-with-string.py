s, q = input().split()
s, q = list(s), int(q)

for _ in range(q):
    string = input().split()

    string[0] = int(string[0])

    if string[0] == 1:
        string[1] = int(string[1])
        string[2] = int(string[2])

        a, b = s[string[1] - 1], s[string[2] - 1]

        s[string[1] - 1] = b
        s[string[2] - 1] = a

        print("".join(s))
    
    elif string[0] == 2:

        a, b = string[1], string[2]

        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
        
        print("".join(s))