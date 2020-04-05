def make_choice():
    print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit
Your choice:""")
    return int(input())

def transpose_along():
    print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice:""")
    return int(input())

def get_matrix(num_rows):
    matrix = list()
    for i in range(int(num_rows)):
        row = input().split()
        matrix.append(row)
        row = list()
    return matrix

def check_can_sum(f_size, s_size):
    f_num_rows = f_size[0]
    f_num_columns = f_size[1]
    s_num_rows = s_size[0]
    s_num_columns = s_size[1]
    if f_num_rows == s_num_rows and f_num_columns == s_num_columns:
        return True
    else:
        return False

def add_matrices(f_matrix, s_matrix):
    sum_row = list()
    sum_matrix = list()

    for i in range(len(f_matrix)):
        for j in range(len(f_matrix[0])):
            if float(f_matrix[0][0]).is_integer() and float(s_matrix[0][0]).is_integer():
                num1 = int(f_matrix[i][j])
                num2 = int(s_matrix[i][j])
                cell = num1 + num2
                sum_row.append(cell)
            else:
                num1 = float(f_matrix[i][j])
                num2 = float(s_matrix[i][j])
                cell = num1 + num2
                sum_row.append(cell)
        else:
            sum_matrix.append(sum_row)
            sum_row = list()
    return sum_matrix

def matrix_printer(matrix):
    print("The result is: ")
    for row in range(len(matrix)):
        print(*(str(item) for item in matrix[row]), sep=" ")

def multiply_by_constant(matrix, constant):
    sum_row = list()
    sum_matrix = list()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (float(matrix[0][0])).is_integer and (float(constant)).is_integer:
                num = int(matrix[i][j])
                cell = num * int(constant)
                sum_row.append(int(cell))
            else:
                num = float(matrix[i][j])
                cell = num * float(constant)
                sum_row.append(cell)
        else:
            sum_matrix.append(sum_row)
            sum_row = list()
    return sum_matrix

def check_can_multiply(f_size, s_size):
    f_num_columns = f_size[1]
    s_num_rows = s_size[0]
    if f_num_columns == s_num_rows:
        return True
    else:
        return False

def multiple_matrices(f_matrix, s_matrix):
    multipled_matrix = list()
    for n in range(len(f_matrix)):
        row = list()
        for m in range(len(s_matrix[0])):
            cell = 0
            if float(f_matrix[0][0]).is_integer() and float(s_matrix[0][0]).is_integer():
                for index in range(len(s_matrix)):
                    num1 = int(f_matrix[n][index])
                    num2 = int(s_matrix[index][m])
                    cell += num1 * num2
                else:
                    row.append(cell)
                    cell = 0
            else:
                for index in range(len(s_matrix)):
                    num1 = float(f_matrix[n][index])
                    num2 = float(s_matrix[index][m])
                    cell += num1 * num2
                else:
                    row.append(cell)
                    cell = 0
        else:
            multipled_matrix.append(row)
            row = list()
    return multipled_matrix

def check_type(matrix):
    if isinstance(matrix[0][0], int):
        return True

def get_determinant(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return None
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]* matrix[1][1] - matrix[0][1]* matrix[1][0]
    else:
        determinant = 0
        for i in range(len(matrix)):
            determinant += matrix[0][i] * get_determinant((get_submatrix(matrix, i)) * pow(-1, i))

def get_submatrix(matrix, index):
    submatrix = list()
    for _ in range(len(matrix) - 1):
        submatrix.append([])
    for i in range(1, len(matrix)):
        for j in range(len(matrix)):
            if index != j:
                submatrix[i - 1].append(matrix[i][j])
    return submatrix

def calculate_minors(minors):
    n = len(minors)
    if n == 1:
        return int(minors[0])
    else:
        return int(minors[-1]) * calculate_minors(minors[:n:])

def processor():
    while True:
        choice = make_choice()
        if choice == 0:
            return False
        elif choice == 1 or choice == 3:
            # get first matrix
            print("Enter size of first matrix: ")
            f_size = list(input().split())
            f_num_rows = f_size[0]
            print("Enter first matrix: ")
            f_matrix = get_matrix(f_num_rows)
            # get second matrix
            print("Enter size of second matrix: ")
            s_size = list(input().split())
            s_num_rows = s_size[0]
            print("Enter second matrix: ")
            s_matrix = get_matrix(s_num_rows)

            if choice == 1: # Add matrices
                if check_can_sum(f_size, s_size):
                    sum_matrix = add_matrices(f_matrix, s_matrix)
                    matrix_printer(sum_matrix)
                    continue
                else:
                    print("The operation cannot be performed.")
                    continue
            else: # Multiply matrices
                if check_can_multiply(f_size, s_size):
                    multipled_matrix = multiple_matrices(f_matrix, s_matrix)
                    matrix_printer(multipled_matrix)
                    continue
                else:
                    print("The operation cannot be performed.")
                    continue
        elif choice == 2:
            print("Enter size of matrix: ")
            size = list(input().split())
            num_rows = size[0]
            print("Enter  matrix: ")
            matrix = get_matrix(num_rows)
            constant = input("Enter constant: ")
            multipled_matrix = multiply_by_constant(matrix, constant)
            matrix_printer(multipled_matrix)
            continue
        elif choice == 4:
            choice = transpose_along()
            print("Enter matrix size: ")
            size = list(input().split())
            num_rows = size[0]
            print("Enter  matrix: ")
            matrix = get_matrix(num_rows)
            transposed_matrix = list()
            row = list()
            if choice == 1:
                for n in range(len(matrix)):
                    for m in range(len(matrix[0])):
                        cell = matrix[m][n]
                        row.append(cell)
                    else:
                        transposed_matrix.append(row)
                        row = list()
                else:
                    matrix_printer(transposed_matrix)
                    continue
            elif choice == 2:
                for n in range(1, len(matrix) + 1):
                    for m in range(1, len(matrix[0]) + 1):
                        cell = matrix[-m][-n]
                        row.append(cell)
                    else:
                        transposed_matrix.append(row)
                        row = list()
                else:
                    matrix_printer(transposed_matrix)
                    continue
            elif choice == 3:
                for n in range(len(matrix)):
                    for m in range(1, len(matrix[0])+ 1):
                        cell = matrix[n][-m]
                        row.append(cell)
                    else:
                        transposed_matrix.append(row)
                        row = list()
                else:
                    matrix_printer(transposed_matrix)
                    continue
            else:
                for n in range(1, len(matrix) + 1):
                    for m in range(len(matrix[0])):
                        cell = matrix[-n][m]
                        row.append(cell)
                    else:
                        transposed_matrix.append(row)
                        row = list()
                else:
                    matrix_printer(transposed_matrix)
                    continue
        elif choice == 5:
            print("Enter matrix size: ")
            size = list(input().split())
            num_rows = size[0]
            print("Enter  matrix: ")
            matrix = get_matrix(num_rows)
            determinant = get_determinant(matrix)
            print("The result is: ")
            print(determinant)
        else:
            print("Invalid choice")
            continue

processor()
