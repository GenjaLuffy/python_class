matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# value = matrix[0]
# value1 = value[1]
# print(value1)
add = 0
for x in range(len(matrix)):
    # print(matrix[x])
    for y in range(len(matrix[x])):
        # print(matrix[x][y])
        add += matrix[x][y] 
print(add)


product = 1
# for i in range(len(matrix)):
#    product *= matrix[i][i]
# print(product)

c = len(matrix)
for r in range(len(matrix)):
    product *= matrix[r][c-1-r] 
print(product)