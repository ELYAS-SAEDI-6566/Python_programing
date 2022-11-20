def cf (main = str , search = str):
    Count = main.count(search)
    print("Count = ",Count)
    start = 0
    L= []
    for i in range(Count):
        s = main.find(search,start)
        L.append(s+1)
        start = s+1
    print("place = ",L)
#______________________________________________________________________________
Main = str(input("enter main string : "))
Search = str(input("enter search string : "))
#______________________________________________________________________________
cf(Main , Search)
