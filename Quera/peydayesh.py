#از بین ۱ و ۲و ۳ و ۴ کدام در ورودی نیست؟
#Which of 1, 2, 3, and 4 is not the entrance?
def find(num1, num2, num3):
    List = [num1,num2,num3]
    for i in range(1,5):
        if i not in List:
            return i