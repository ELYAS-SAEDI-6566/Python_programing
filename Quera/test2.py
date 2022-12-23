x = str(input())
x = x.split()
s = int(x[0])
e = int(x[1])
way = []
if s == e :
        print("Saal Noo Mobarak!")
        exit()
while(True):
    if s == e :
        for i in way:
            print(i,end="")
        exit()
    else:
        if s > e :
            s -= 1
            way.append("L")
        else :
            s += 1
            way.append("R")