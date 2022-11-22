def cf (main = str , search = str):
    Count = main.count(search)
    print("Count = ",Count)
    start = 0
    L= []
    for i in range(Count):
        s = main.find(search,start)
        L.append(s)
        start = s+1
    print("place = ",L)