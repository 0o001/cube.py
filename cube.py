position = [1,1]

matrix = [ [4,9,2],[3,5,7],[8,1,6] ]

for shift in range(position[0]):
    matrix.insert(0, matrix.pop())

for shift in matrix:
    for loop in range(position[1]):
        shift.insert(0, shift.pop())

print(*matrix, sep='\n')