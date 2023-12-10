def diagonal_max(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("Matris boş və kvadrat olmalıdır.")

    size = len(matrix)
    max_diagonal_element = matrix[0][0]

    for i in range(1, size):
        if matrix[i][i] > max_diagonal_element:
            max_diagonal_element = matrix[i][i]

    return max_diagonal_element

# Matris nümunəsi
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Nəticəni çap et
result = diagonal_max(matrix)
print("Baş diagonalın maksimumu:", result)
