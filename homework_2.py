import random
M,N = int(input("Matrix width (enter number)")),int(input("Matrix height (enter number)"))
matrix = [[random.randrange(-10,10) for y in range(M)] for x in range(N)]
for line in matrix:
    print(line)
print("---------------")
indH = []
indL = []
for lineIndex, line in enumerate(matrix):
    for elemIndex, elem in enumerate(line):
        if elem == 0:
            indH.append(elemIndex)
            indL.append(lineIndex)
for elemL in indL:
    for i in range(len(matrix[elemL])):
        matrix[elemL][i] = 0
for line in matrix:
    for elemH in indH:
        line[elemH] = 0
    print(line)