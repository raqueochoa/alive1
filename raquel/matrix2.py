m = [
[1,1,1],
[1,1,2],
[1,3,1]
]

def sum(matrix):
    suma = 0
    for x in matrix:
        for y in x:
            suma = suma + y
    return suma

def max(matrix):
    max = matrix [0][0]
    for x in matrix:
        for y in x:
            if y >= max:
                max = y
    return max

def min(matrix):
    min = matrix [0][0]
    for x in matrix:
        for y in x:
            a = y
            if y <= a:
                min = y
    return min
