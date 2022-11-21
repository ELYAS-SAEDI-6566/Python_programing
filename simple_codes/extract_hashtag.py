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
    from delete_list_element import delete_list_element
    return delete_list_element(strList , "")
#________________Test code____________________________________#
# text = "this ## is a #sample#test1 #test2 #test3#test4 ##test5"
# print(find_hashtag(text))