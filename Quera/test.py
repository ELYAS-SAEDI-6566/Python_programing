n = int(input())
names = []
for i in range(n) :
    n = input()
    names.append(n.split()[0])
colors = 1
for i in names :
    nameCount = names.count(i)
    if nameCount > colors:
        colors = nameCount
print(colors)