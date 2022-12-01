value = str(input())
nk = value.split(" ")
nk[0] = int(nk[0])
nk[1] = int(nk[1])
i = 1
count = 0
while(True):
    count += 1
    if i+nk[1] > nk[0] :
        x = nk[0] - i
        i = 0
        i += nk[1]-x
    else :
        i += nk[1]
    if i == 1 :
        print(count)
        break