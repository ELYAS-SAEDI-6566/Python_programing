c1 = str(input())
c2 = str(input())
# c1 = "O R"
# c2 = "O G"
c1 = c1.split()
c2 = c2.split()
# print(c1)
# print(c2)
if c1[0] == c1[1]:
    print("YES")
    exit()
if c2[0] == c2[1]:
    print("YES")
    exit()
if c1[0] == c2[1]:
    print("YES")
    exit()
if c1[1] == c2[0]:
    print("YES")
    exit()
print("NO")