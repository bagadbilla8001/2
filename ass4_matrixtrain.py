def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Error: Matrices have different dimensions and cannot be added."
    
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return "Error: Number of columns in first matrix must be equal to number of rows in second matrix."
    
    result = [[sum(a * b for a, b in zip(matrix1_row, matrix2_col)) for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]
    return result

def is_upper_triangular(matrix):
    for i in range(1, len(matrix)):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True

def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])

    # Check all rows
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    
    # Check all columns
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_sum:
            return False
    
    # Check both diagonals
    if sum(matrix[i][i] for i in range(n)) != magic_sum or sum(matrix[i][n - i - 1] for i in range(n)) != magic_sum:
        return False
    
    return True

def input_matrix(rows, cols):
    print(f"Enter {rows}x{cols} matrix:")
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def main():
    choice = 1
    while choice != 0:
        print("\n\n=========Matrix Operations========\n")
        print("1. Add Matrices")
        print("2. Multiply Matrices")
        print("3. Check if Matrix is Upper Triangular")
        print("4. Check if Matrix is Magic Square")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            rows1, cols1 = map(int, input("Enter dimensions of first matrix (rows columns): ").split())
            rows2, cols2 = map(int, input("Enter dimensions of second matrix (rows columns): ").split())

            if cols1 != rows2:
                print("Error: Cannot add matrices with these dimensions.")
                continue

            matrix1 = input_matrix(rows1, cols1)
            matrix2 = input_matrix(rows2, cols2)
            result = add_matrices(matrix1, matrix2)
            print("Result:")
            for row in result:
                print(row)

        elif choice == 2:
            rows1, cols1 = map(int, input("Enter dimensions of first matrix (rows columns): ").split())
            rows2, cols2 = map(int, input("Enter dimensions of second matrix (rows columns): ").split())

            result = multiply_matrices(matrix1, matrix2)
            if isinstance(result, str):
                print(result)
            else:
                print("Result:")
                for row in result:
                    print(row)

        elif choice == 3:
            rows, cols = map(int, input("Enter dimensions of matrix (rows columns): ").split())
            matrix = input_matrix(rows, cols)
            if is_upper_triangular(matrix):
                print("The matrix is upper triangular.")
            else:
                print("The matrix is not upper triangular.")

        elif choice == 4:
            rows, cols = map(int, input("Enter dimensions of matrix (rows columns): ").split())
            matrix = input_matrix(rows, cols)
            if is_magic_square(matrix):
                print("The matrix is a magic square.")
            else:
                print("The matrix is not a magic square.")

        elif choice == 0:
            print("Exiting...")

if __name__ == "__main__":
    main()
