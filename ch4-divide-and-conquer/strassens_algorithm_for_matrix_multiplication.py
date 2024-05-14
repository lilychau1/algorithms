from typing import List
def strassen_multiply_square_matrix(matrix_a: List[List[int]], matrix_b: List[List[int]]) -> None:
    """
    Performs matrix multiplication using Strassen's algorithm.

    Args:
        matrix_a (List[List[int]]): The first matrix to be multiplied.
        matrix_b (List[List[int]]): The second matrix to be multiplied.

    Returns:
        List[List[int]]: The resulting product matrix.

    Raises:
        ValueError: If the dimensions of the input matrices are not compatible for multiplication.

    Note:
        - This function assumes that the input matrices are square matrices.
        - The dimensions of the input matrices must be powers of 2.
        - If the dimensions of the input matrices are not powers of 2, the matrices should be padded with zeros.
        - This function recursively divides the matrices into submatrices and performs multiplication using Strassen's algorithm.

    Example:
        A = [[1, 2],
             [3, 4]]
        B = [[1, 2],
             [3, 4]]
        C = strassen_multiply_square_matrix(A, B)
        # Output:
        # [[7, 10],
        # [15, 22]]
    """
    n = len(matrix_a)
    
    # Base case: if matrices are 1x1, compute their product directly
    if n == 1:
        return [[matrix_a[0][0] * matrix_b[0][0]]]
    
    # Divide matrices into submatrices
    new_size = n // 2
    a11 = [row[:new_size] for row in matrix_a[:new_size]]
    a12 = [row[new_size:] for row in matrix_a[:new_size]]
    a21 = [row[:new_size] for row in matrix_a[new_size:]]
    a22 = [row[new_size:] for row in matrix_a[new_size:]]
    
    b11 = [row[:new_size] for row in matrix_b[:new_size]]
    b12 = [row[new_size:] for row in matrix_b[:new_size]]
    b21 = [row[:new_size] for row in matrix_b[new_size:]]
    b22 = [row[new_size:] for row in matrix_b[new_size:]]

    # Calculate intermediate metrices
    s1 = [[b12[i][j] - b22[i][j] for j in range(new_size)] for i in range(new_size)]
    s2 = [[a11[i][j] + a12[i][j] for j in range(new_size)] for i in range(new_size)]
    s3 = [[a21[i][j] + a22[i][j] for j in range(new_size)] for i in range(new_size)]
    s4 = [[b21[i][j] - b11[i][j] for j in range(new_size)] for i in range(new_size)]
    s5 = [[a11[i][j] + a22[i][j] for j in range(new_size)] for i in range(new_size)]
    s6 = [[b11[i][j] + b22[i][j] for j in range(new_size)] for i in range(new_size)]
    s7 = [[a12[i][j] - a22[i][j] for j in range(new_size)] for i in range(new_size)]
    s8 = [[b21[i][j] + b22[i][j] for j in range(new_size)] for i in range(new_size)]
    s9 = [[a11[i][j] - a21[i][j] for j in range(new_size)] for i in range(new_size)]
    s10 = [[b11[i][j] + b12[i][j] for j in range(new_size)] for i in range(new_size)]
    
    # Recursively calculate sub-produts
    p1 = strassen_multiply_square_matrix(a11, s1)
    p2 = strassen_multiply_square_matrix(s2, b22)
    p3 = strassen_multiply_square_matrix(s3, b11)
    p4 = strassen_multiply_square_matrix(a22, s4)
    p5 = strassen_multiply_square_matrix(s5, s6)
    p6 = strassen_multiply_square_matrix(s7, s8)
    p7 = strassen_multiply_square_matrix(s9, s10)
    
    # Combine sub-products to form the final product matrix
    c11 = [[p5[i][j] + p4[i][j] - p2[i][j] + p6[i][j] for j in range(new_size)] for i in range(new_size)]
    c12 = [[p1[i][j] + p2[i][j] for j in range(new_size)] for i in range(new_size)]
    c21 = [[p3[i][j] + p4[i][j] for j in range(new_size)] for i in range(new_size)]
    c22 = [[p5[i][j] + p1[i][j] - p3[i][j] - p7[i][j] for j in range(new_size)] for i in range(new_size)]
    
    # Construct the final product  matrix
    product_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(new_size):
        for j in range(new_size):
            product_matrix[i][j] = c11[i][j]
            product_matrix[i][j + new_size] = c12[i][j]
            product_matrix[i + new_size][j] = c21[i][j]
            product_matrix[i + new_size][j + new_size] = c22[i][j]
    
    return product_matrix
 
if __name__ == '__main__':
    A = [
        [1, 2],
        [3, 4],
    ]

    B = [
        [1, 2],
        [3, 4],
    ]

    C = strassen_multiply_square_matrix(A, B)
    
    print("------- Strassen's algorithm -------")
    
    for row in C:
        print(row)
       
    # Expected results: 
    # [7, 10]
    # [11, 22]