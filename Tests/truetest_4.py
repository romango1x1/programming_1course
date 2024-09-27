class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def multiply_matrices(self, other_matrix):
        if self.cols != other_matrix.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

        res = [[0 for _ in range(other_matrix.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(other_matrix.cols):
                for k in range(self.cols):
                    res[i][j] += self.matrix[i][k] * other_matrix.matrix[k][j]
        return res

    def multiply_matrix_vector(self, vector):
        res = [0 for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                res[i] += self.matrix[i][j] * vector[j]
        return res

    def multiply_vector_matrix(self, vector):
        res = [0 for _ in range(self.cols)]

        for i in range(self.cols):
            for j in range(self.rows):
                res[i] += vector[j] * self.matrix[j][i]
        return res

    def swap_rows(self, row1, row2):
        self.matrix[row1], self.matrix[row2] = self.matrix[row2], self.matrix[row1]

    def swap_columns(self, col1, col2):
        for i in range(self.rows):
            self.matrix[i][col1], self.matrix[i][col2] = self.matrix[i][col2], self.matrix[i][col1]

    def get_row(self, index):
        return self.matrix[index]

    def multiply_vector_by_scalar(self, vector, scalar):
        return [scalar * element for element in vector]

    def subtract_vector_from_rows(self, vector):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] -= vector[j]

    def upper_triangle_transform(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if i < j:
                    matrix[i][j] = 0

        return matrix

    def matrix_rank(self):
        rank = 0

        for i in range(self.rows):
            non_zero_els = [el for el in self.matrix[i] if el != 0]
            if non_zero_els:
                rank += 1
        return rank

    def matrix_determinant(self):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square for determinant calculation")

        det = 1

        for i in range(self.rows):
            pivot = self.matrix[i][i]
            if pivot == 0:
                return 0

            det *= pivot

            for j in range(i + 1, self.rows):
                factor = self.matrix[j][i] / pivot
                for k in range(i, self.cols):
                    self.matrix[j][k] -= factor * self.matrix[i][k]

        return det


matrix = [
    [5, 7, 10],
    [4, 9, 6],
    [1, 2, 1]
]

other_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

vector_data = [1, 2, 3]

matrix_operations = MatrixOperations(matrix)
other_matrix = MatrixOperations(other_matrix)

print("Original Matrix:")
matrix_operations.print_matrix()

print("\nMultiply Matrices:")
res_matrix = matrix_operations.multiply_matrices(other_matrix)
for row in res_matrix:
    print(row)

print("\nMultiply Matrix by Vector:")
res_vector = matrix_operations.multiply_matrix_vector(vector_data)
print(res_vector)

print("\nMultiply Vector by Matrix:")
res_vector = matrix_operations.multiply_vector_matrix(vector_data)
print(res_vector)

print("\nSwap Rows:")
matrix_operations.swap_rows(0, 2)
matrix_operations.print_matrix()

print("\nSwap Columns:")
matrix_operations.swap_columns(0, 2)
matrix_operations.print_matrix()

print("\nGet Row:")
row = matrix_operations.get_row(1)
print(row)

print("\nMultiply Vector by Scalar:")
res_vector = matrix_operations.multiply_vector_by_scalar(vector_data, 2)
print(res_vector)

print("\nSubtract Vector from Rows:")
matrix_operations.subtract_vector_from_rows(vector_data)
matrix_operations.print_matrix()

print("\nUpper Triangle Transformation:")
matrix_operations.upper_triangle_transform()
matrix_operations.print_matrix()

print("\nMatrix Rank:")
rank = matrix_operations.matrix_rank()
print(rank)

print("\nMatrix Determinant:")
determinant = matrix_operations.matrix_determinant()
print(determinant)
