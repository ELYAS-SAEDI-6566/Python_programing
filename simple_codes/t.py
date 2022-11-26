def delete_element(List = [], element = int):
    Count  = List.count(element)
    for i in range(Count):
        List.remove(element)
    return List
#______________________________Main_____________________________#
def find_hashtag(string):
    strList = string.split()
    result = []
    for word in strList:
        if "#" in word:
            result.append(word)
    strList = result
    result = []
    for hashWord in strList:
        result =  result + hashWord.split("#")[1:]
    strList = result
    return delete_element(strList , "")
#______________________________________________________________
text = str(input("Enter the text : "))
#text = "this ## is a #sample#test1 ###python #test2 #test3#test4 #is_hashtag not_hashtag##test5"
print("The main text is : " + text)
print("Hashtags list : " , find_hashtag(text))