x = int(input())
result = True
if x == 1:
    print("fard")
    exit()
if x%2 == 0:
    print("fard")
else:
    for i in range(2,x):
        if x%i == 0:
            result = False
    if result :
        print("zoj")
    else:
        print("fard")