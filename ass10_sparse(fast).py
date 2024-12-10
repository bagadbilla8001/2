class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []

    def add_element(self, row, col, value):
        if value != 0:
            self.data.append((row, col, value))

    def transpose(self):
        transposed = SparseMatrix(self.cols, self.rows)
        for row, col, value in self.data:
            transposed.add_element(col, row, value)
        return transposed

    def fast_transpose(self):
        transposed = SparseMatrix(self.cols, self.rows)
        count = [0] * self.cols

        for _, col, _ in self.data:
            count[col] += 1

        index = [0] * self.cols
        for i in range(1, self.cols):
            index[i] = index[i - 1] + count[i - 1]

        for row, col, value in self.data:
            pos = index[col]
            transposed.data.insert(pos, (col, row, value))
            index[col] += 1

        return transposed

    def __str__(self):
        matrix = [[0] * self.cols for _ in range(self.rows)]
        for row, col, value in self.data:
            matrix[row][col] = value
        return "\n".join(["\t".join(map(str, row)) for row in matrix])

# Example usage
sparse = SparseMatrix(3, 3)
sparse.add_element(0, 1, 5)
sparse.add_element(1, 0, 3)
sparse.add_element(2, 2, 2)

print("Original Sparse Matrix:")
print(sparse)

transpose = sparse.transpose()
print("\nTranspose:")
print(transpose)

fast_transpose = sparse.fast_transpose()
print("\nFast Transpose:")
print(fast_transpose)
