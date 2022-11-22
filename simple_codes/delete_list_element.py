#______Main definition______#
def delete_list_element(List = [], element = int):
    Count  = List.count(element)
    for i in range(Count):
        List.remove(element)
    return List