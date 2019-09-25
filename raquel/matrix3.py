def promedio(matrix):
    suma = 0
    count = 0.0
    for x in matrix:
        for y in x:
            suma = suma + y
             count = count + 1
    return suma/count
