def create(I = int , J = int):
    import random
    matrix = []
    for i in range(I):
        row = []
        for j in range(J):
            row.append(str(random.randrange(100)))
        matrix.append(row)
    return matrix
def element_detail(matrix , element):
    List_of_details = []
    i = 0 ; j = 0
    for row in matrix:
        j = 0
        for column in row :
            if column == element :
                List_of_details.append([i,j])
            j += 1
        i += 1
    return List_of_details
