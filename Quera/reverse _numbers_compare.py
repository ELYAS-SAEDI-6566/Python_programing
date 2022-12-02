#Reverse two numbers and compare them
num1 = str(input())
num2 = str(input())
num1L = []
num2L = []
for i in num1 :
    num1L.append(i)
for i in num2 :
    num2L.append(i)
num1L.reverse()
num2L.reverse()
num1R = ""
num2R = ""
for i in num1L :
    num1R += i
for i in num2L :
    num2R += i
if num1R > num2R :
    print(f"{num2} < {num1}")
elif num2R > num1R :
    print (f"{num1} < {num2}")
else :
    print(f"{num1} = {num2}")