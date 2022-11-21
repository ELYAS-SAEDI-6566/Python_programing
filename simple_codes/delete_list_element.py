#______Main definition______#
def delete_list_element(List = [], element = int):
    Count  = List.count(element)
    for i in range(Count):
        List.remove(element)
    return List
#___________________________________________________________________________
def make_list():
    import random
    L1 = []
    L2 = []
    for i in range(6):
        if i < 3:
            L1.append(random.randrange(100))
        else:
            L2 = L2 + L1
    return L2
#__________________________________________________________________________
List = make_list()
print("The list is ",List)
element = input("Which one should be remove ? : ")
error = "The element isnt in list  \nEnter one of list : "
while True:
    try:
        element = int(element)
    except ValueError:
        element = input(error)
        continue
    if element in List:
        break
    else:
        element = input(error)
        continue
print("New list : ",delete_list_element(List , element))