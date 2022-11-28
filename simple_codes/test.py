program_num = input("""[1] Count find def list     [2] Delete list element
[3] Find hashtags           [4] Reverse text words
[5] matrix element detail
Enter the number of program you want to run : """)
match program_num:
    case "1" :
        Main = str(input("enter main string : "))
        Search = str(input("enter search string : "))
        import count_find_def_list
        count_find_def_list.cf(Main , Search)
    case "2" :
        import make_list
        List = make_list.numbers_type_str()
        print("The list is ",List)
        element = str(input("Which one should be remove ? : "))
        error = "The element isnt in list  \nEnter one of list : "
        while True:
            if element in List:
                break
            element = str(input(error))
        import delete_list_element
        print("New list : ",delete_list_element.delete_element(List , str(element)))
    case "3" :
        text = str(input("Enter the text : "))
        #text = "this is a #sample ## #test . not_hashtag1# ### ###python #test3#test4 not_hashtag##test5"
        print("The main text is : " + text)
        import extract_hashtag
        print("Hashtags list : " , extract_hashtag.find_hashtag(text))
    case "4" :
        text = str(input("Enter the text :"))
        #text = "I Am from Iran it iS rainy and i like rain"
        import edit_text
        print(edit_text.reverse(text))
    case "5" :
        import matrix
        matrix1 = matrix.create(10,10)
        for i in matrix1 :
            print(i)
        element = str(input("Select element : "))
        print(matrix.element_detail(matrix1 , element))