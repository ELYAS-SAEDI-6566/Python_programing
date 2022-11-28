#دریافت لیستی از اعداد و جدا کردن زوج و فرد
#Get a list of numbers and separate even and odd
def separator(ls) :
    hamid_list = []
    hamed_list = []
    for number in ls :
        if number%2 == 0 :
            hamid_list.append(number)
        else:
            hamed_list.append(number)
    tuple = (hamid_list,hamed_list)
    return tuple