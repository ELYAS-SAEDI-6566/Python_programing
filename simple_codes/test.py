program_num = input("""[1] count find def list     [2] delete list element
Enter the number of program you want to run : """)
match program_num:
    case "1" :
        Main = str(input("enter main string : "))
        Search = str(input("enter search string : "))
        import count_find_def_list
        count_find_def_list.cf(Main , Search)
    case "2" :
        import make_list
        List = make_list.type_int()
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
        import delete_list_element
        print("New list : ",delete_list_element(List , element))
    case "3" :
        