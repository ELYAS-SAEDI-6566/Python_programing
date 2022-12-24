# """In Digikala, some kind of compression is used to store some numeric strings so that no one can get the original numeric string from the generated output.
# Of course, here we are aware of the fact that this method has conflicts; 
# That is, we ignore that several different inputs may produce the same output! It should be noted that the numeric string contains only digits 0 to 9. 
# The algorithm counts the number of repetitions of all digits in the string, removes the repeated digits, 
# and writes the number of repetitions of each digit (provided that it is repeated at least 2 times) in the input string, and finally the numeric string as Arranges ascending. 
# This process is repeated on the obtained output again and continues until the final output does not differ from the output of the previous step.
# """
last_num = str(input())
def compresssion(num):
    save = ""
    c = ""
    for i in num :
        if i not in save :
            save += i
            if num.count(i) > 1 :
                c += str(num.count(i))
    save = save+c
    num = ""
    for i in sorted(save):
        num += i
    return num
new_num = compresssion(last_num)
while(new_num != last_num):
    last_num = new_num
    new_num = compresssion(last_num)
print(new_num)
# ________example__________
# input : 442254545
# output : 22345