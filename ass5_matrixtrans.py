def transpose(matrix):
    """
    Computes the transpose of a matrix.
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def add_matrices(matrix1, matrix2):
    """
    Adds two matrices.
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Error: Matrices have different dimensions and cannot be added."
    
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2):
    """
    Multiplies two matrices.
    """
    if len(matrix1[0]) != len(matrix2):
        return "Error: Number of columns in first matrix must be equal to number of rows in second matrix."
    
    return [[sum(a * b for a, b in zip(matrix1_row, matrix2_col)) for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]

def find_saddle_point(matrix):
    """
    Determines if a matrix has a saddle point.
    A saddle point is defined as an element that is the smallest in its row and largest in its column.
    """
    for i in range(len(matrix)):
        row_min = min(matrix[i])
        min_col_index = matrix[i].index(row_min)
        is_saddle_point = all(matrix[i][min_col_index] >= matrix[k][min_col_index] for k in range(len(matrix)))
        
        if is_saddle_point:
            return (i, min_col_index)
    
    return "No saddle point found."

def input_matrix(rows, cols):
    """
    Helper function to input a matrix.
    """
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
        print("1. Transpose of a matrix")
        print("2. Add Matrices")
        print("3. Multiply Matrices")
        print("4. Find Saddle Point")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            rows, cols = map(int, input("Enter dimensions of matrix (rows columns): ").split())
            matrix = input_matrix(rows, cols)
            transposed = transpose(matrix)
            print("Transposed Matrix:")
            for row in transposed:
                print(row)

        elif choice == 2:
            rows1, cols1 = map(int, input("Enter dimensions of first matrix (rows columns): ").split())
            rows2, cols2 = map(int, input("Enter dimensions of second matrix (rows columns): ").split())

            if cols1 != rows2:
                print("Error: Cannot add matrices with these dimensions.")
                continue

            matrix1 = input_matrix(rows1, cols1)
            matrix2 = input_matrix(rows2, cols2)
            result = add_matrices(matrix1, matrix2)
            if isinstance(result, str):
                print(result)
            else:
                print("Result:")
                for row in result:
                    print(row)

        elif choice == 3:
            rows1, cols1 = map(int, input("Enter dimensions of first matrix (rows columns): ").split())
            rows2, cols2 = map(int, input("Enter dimensions of second matrix (rows columns): ").split())

            if cols1 != rows2:
                print("Error: Number of columns in first matrix must be equal to number of rows in second matrix.")
                continue

            matrix1 = input_matrix(rows1, cols1)
            matrix2 = input_matrix(rows2, cols2)
            result = multiply_matrices(matrix1, matrix2)
            if isinstance(result, str):
                print(result)
            else:
                print("Result:")
                for row in result:
                    print(row)

        elif choice == 4:
            rows, cols = map(int, input("Enter dimensions of matrix (rows columns): ").split())
            matrix = input_matrix(rows, cols)
            saddle_point = find_saddle_point(matrix)
            if saddle_point == "No saddle point found.":
                print(saddle_point)
            else:
                print(f"Saddle point found at row {saddle_point[0]}, column {saddle_point[1]}.")

        elif choice == 0:
            print("Exiting...")

if __name__ == "__main__":
    main()
