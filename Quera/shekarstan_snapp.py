#This question was so hard to understanding. 
#We want sum the travels in snapp
line1 = str(input())
l = line1.split()
matlist = []
for i in range(int(l[0])) :
    matlist.append(input())
tralist = []
for i in range(int(l[1])) :
    tralist.append(input())

NM = line1.split()
matrix = []
for i in matlist :
    matrix.append(i.split())
sum = 0
for i in tralist :
    k = i.split()
    sum += int(matrix[int(k[0]) - 1][int(k[1]) -1])    
print(sum)
#____________example input___________#
# 4 4
# 277 30 971 789
# 65 379 158 855
# 892 92 267 454
# 449 293 735 533
# 2 3
# 4 3
# 1 3
# 2 4
#_________________output__________________#
#2719