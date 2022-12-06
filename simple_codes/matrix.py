def create(I = int , J = int):
    import random
    matrix = []
    for i in range(I):
        row = []
        for j in range(J):
            row.append(str(random.randrange(100)))
        matrix.append(row)
    return matrix
def element_position(matrix , element):
    List_of_positions = []
    for row in matrix:
        for column in row :
            if column == element :
                List_of_positions.append([matrix.index(row),row.index(column)])
    return List_of_positions