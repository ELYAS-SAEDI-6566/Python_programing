import random
import string
for i in range(16):
    ch = [random.randrange(10),random.choice(string.ascii_letters)]
    print(random.choice(ch), end = "")