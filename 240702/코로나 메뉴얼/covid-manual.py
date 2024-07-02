p1 = input().split()
p2 = input().split()
p3 = input().split()

if p1[0] == "Y" and int(p1[1]) >= 37 or p2[0] == "Y" and int(p1[1]) >= 37 or p3[0] == "Y" and int(p1[1]) >= 37:
    if ((p1[0] == "Y" and int(p1[1]) >= 37) and (p2[0] == "Y" and int(p2[1]) >= 37)
    or (p1[0] == "Y" and int(p1[1])) and (p3[0] == "Y" and int(p3[1]) >= 37) 
    or (p2[0] == "Y" and int(p2[1]) >= 37) and (p3[0] == "Y" and int(p3[1]) >= 37)):
        print("E")
    else:
        print("N")
else:
    print("N")