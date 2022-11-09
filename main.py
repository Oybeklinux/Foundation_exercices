transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

print(f"Matritsa: {matrix}")

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(f"Transponirlangan matritsa: {transposed}")