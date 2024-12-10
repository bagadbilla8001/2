class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Dictionary to store non-zero elements in the format {(row, col): value}
        self.elements = {}

    def set_element(self, row, col, value):
        """Set an element in the matrix."""
        if value != 0:
            self.elements[(row, col)] = value

    def get_element(self, row, col):
        """Get an element in the matrix, returns 0 if not present."""
        return self.elements.get((row, col), 0)

    def display(self):
        """Display the matrix."""
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.get_element(i, j), end=" ")
            print()

    def transpose(self):
        """Transpose the sparse matrix."""
        transposed = SparseMatrix(self.cols, self.rows)
        for (r, c), v in self.elements.items():
            transposed.set_element(c, r, v)
        return transposed

    def add(self, other):
        """Add two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices dimensions must match for addition")

        result = SparseMatrix(self.rows, self.cols)

        # Add elements from self
        for (r, c), v in self.elements.items():
            result.set_element(r, c, v)

        # Add elements from other
        for (r, c), v in other.elements.items():
            result.set_element(r, c, result.get_element(r, c) + v)

        return result

# Example usage
def main():
    # Matrix 1 (3x3)
    mat1 = SparseMatrix(3, 3)
    mat1.set_element(0, 0, 5)
    mat1.set_element(1, 2, 8)
    mat1.set_element(2, 1, 6)

    # Matrix 2 (3x3)
    mat2 = SparseMatrix(3, 3)
    mat2.set_element(0, 2, 3)
    mat2.set_element(1, 1, 4)
    mat2.set_element(2, 0, 7)

    print("Matrix 1:")
    mat1.display()

    print("\nMatrix 2:")
    mat2.display()

    # Transpose of Matrix 1
    transposed = mat1.transpose()
    print("\nTranspose of Matrix 1:")
    transposed.display()

    # Addition of Matrix 1 and Matrix 2
    added = mat1.add(mat2)
    print("\nAddition of Matrix 1 and Matrix 2:")
    added.display()

if __name__ == "__main__":
    main()
