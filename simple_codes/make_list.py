def type_int():
    import random
    L1 = []
    L2 = []
    for i in range(3):
            L1.append(random.randrange(100))
    for i in range(3):
            L2 = L2 + L1
    return L2