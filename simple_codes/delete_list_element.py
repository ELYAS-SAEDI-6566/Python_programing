def delete_element(List = [], element = ""):
    Count  = List.count(element)
    for i in range(Count):
        List.remove(element)
    return List