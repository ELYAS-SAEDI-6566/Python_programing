def test(names = list):
    colors = 1
    for i in names :
        nameCount = names.count(i)
        if nameCount > colors:
            colors = nameCount
    print(colors)
test(['bagher','bagher','nader','nader','steve'])
test(['bagher','bagher','bagher','alfred','alfred'])
test(['freddie','brian','roger'])
test(['amir','amir','amir','amir','freddie','brian','roger'])