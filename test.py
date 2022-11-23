program_num = input("""[1] Creat a password
Enter the number of program you want to run : """)
match program_num:
    case "1" :
        import password_creator
        print(password_creator.create_char(16))