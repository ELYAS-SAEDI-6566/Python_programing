def numbers_type_int():
        import random
        L1 = []
        L2 = []
        for i in range(3):
                L1.append(random.randrange(100))
        for i in range(3):
                L2 = L2 + L1
        return L2
def numbers_type_str():
        L1 = numbers_type_int()
        L2 = []
        for i in L1:
                L2.append(str(i))
        return L2