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
    import delete_list_element
    return delete_list_element.delete_element(strList , "")