#Reverse two numbers and compare them
num1 = str(input())
num2 = str(input())
num1R = num1[::-1]
num2R = num2[::-1]
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
