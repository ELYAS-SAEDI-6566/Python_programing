program_num = input("""[1] Count find def list     [2] Delete list element
[3] Find hashtags           [4] Reverse text words
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
        print("New list : ",delete_list_element.delete_element(List , element))
    case "3" :
        text = "this ## is a #sample#test1 ###python #test2 #test3#test4 #is_hashtag not_hashtag##test5"
        print("The main text is : " + text)
        import extract_hashtag
        print("Hashtags list : " , extract_hashtag.find_hashtag(text))
    case "4" :
        text = "I Am from Iran it iS rainy and i like rain"
        import edit_text
        print(edit_text.reverse(text))