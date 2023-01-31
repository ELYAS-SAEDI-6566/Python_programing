def create_char(number):
    import random
    import string
    password = ""
    for i in range(number):
        password += random.choice([str(random.randrange(10)) , random.choice(string.ascii_letters)])
    return password
print(create_char(16))