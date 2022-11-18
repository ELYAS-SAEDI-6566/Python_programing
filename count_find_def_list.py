def cf (main = str , serch = str):
    Count = main.count(serch)
    print("Count = ",Count)
    start = 0
    L= []
    for i in range(Count):
        s = main.find(serch,start)
        L.append(s+1)
        start = s+1
    print("place = ",L)
#______________________________________________________________________________
Main = str(input("enter main string : "))
Serch = str(input("enter serch string : "))
#______________________________________________________________________________
cf(Main , Serch)
