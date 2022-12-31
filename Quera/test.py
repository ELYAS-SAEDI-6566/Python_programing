value = str(input())
nk = value.split()
n = int(nk[0])
m = int(nk[1])
row1 = ""
row2 = ""
#_______________________#
for i in range(m):
    row1 += "X"
for i in range(m):
    row1 += "."
for i in range(m):
    row1 += "X"
#_______________________#
for i in range(m):
    row2 += "."
for i in range(m):
    row2 += "X"
for i in range(m):
    row2 += "."
#_______________________#
result = []
for i in range(n):
    result.append(row1)
for i in range(n):
    result.append(row2)
for i in range(n):
    result.append(row1)
#_________________________#
for i in result:
    print(i)