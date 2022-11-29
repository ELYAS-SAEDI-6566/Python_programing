#کم کردن عدد بزرگ تر از کوچک تر
#Subtract the larger number from the smaller number
def game(number):
    L = []
    for i in str(number):
        L.append(int(i))
    if L[0] > L[1] :
        return L[0]-L[1]
    elif L[1] > L[0] :
        return L[1]-L[0]
    else :
        return 0