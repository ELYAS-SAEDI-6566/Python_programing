def type_int():
    import random
    L1 = []
    L2 = []
    for i in range(6):
        if i < 3:
            L1.append(random.randrange(100))
        else:
            L2 = L2 + L1
    return L2