#______Main definition______#
def delete_list_element(List = [], element = int):
    Count  = List.count(element)
    for i in range(Count):
        List.remove(element)
    return List
#______________Test code______________#
# import make_list
# List = make_list.type_int()
# print("The list is ",List)
# element = input("Which one should be remove ? : ")
# error = "The element isnt in list  \nEnter one of list : "
# while True:
#     try:
#         element = int(element)
#     except ValueError:
#         element = input(error)
#         continue
#     if element in List:
#         break
#     else:
#         element = input(error)
#         continue
# print("New list : ",delete_list_element(List , element))
