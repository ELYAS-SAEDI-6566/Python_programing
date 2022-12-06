def find(matrix , element):
    for i in matrix:
        for j in i :
            if j == element :
                return [matrix.index(i),i.index(j)]

m = [[20,36,5],[48,67,88],[7,97,33]]
print(m)
n = int(input("select element "))
print(find(m,n))