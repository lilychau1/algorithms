from typing import List
def multiply_square_matrix_recursive(matrix_a: List[List[int]], matrix_b: List[List[int]], matrix_c: List[List[int]], n: int) -> None:
    """
    Multiply two square matrices using a recursive algorithm.

    Args:
    - matrix_a (List[List[int]]): The first input square matrix.
    - matrix_b (List[List[int]]): The second input square matrix.
    - matrix_c (List[List[int]]): The output square matrix to store the result of multiplication.
    - n (int): The size of the matrices (number of rows or columns).

    Returns:
    None: The result is stored in the `matrix_c` parameter.

    This function multiplies two square matrices `matrix_a` and `matrix_b` using a recursive
    divide-and-conquer approach. The matrices are divided into smaller submatrices until the
    base case of 1x1 matrices is reached, at which point the multiplication is computed directly.
    The resulting product is stored in the `matrix_c` parameter.

    Example:
    A = [
        [1, 2],
        [3, 4],
    ]
    B = [
        [1, 2],
        [3, 4],
    ]
    C = [[0, 0], [0, 0]]
    multiply_square_matrix_recursive(A, B, C, 2)
    # Output:
    # C = [
    #     [7, 10],
    #     [15, 22]
    # ]
    """
    # Base case: if matrices are 1x1, compute their product directly
    if n == 1:
        matrix_c[0][0] += matrix_a[0][0] * matrix_b[0][0]
        return
    
    # Divide matrices into submatrices
    new_size = n//2
    submatrix_a11 = [[0 for _ in range(new_size)] for _ in range(new_size)]
    submatrix_a12 = [[0 for _ in range(new_size)] for _ in range(new_size)]
    submatrix_a21 = [[0 for _ in range(new_size)] for _ in range(new_size)]
    submatrix_a22 = [[0 for _ in range(new_size)] for _ in range(new_size)]
    submatrix_b11 = [[0 for _ in range(new_size)] for _ in range(new_size)]
    submatrix_b12 = [[0 for _ in range(new_size)] for _ in range(new_size)]
    submatrix_b21 = [[0 for _ in range(new_size)] for _ in range(new_size)]
    submatrix_b22 = [[0 for _ in range(new_size)] for _ in range(new_size)]
    
    # Copy each element in matrices A and B to the submatrices
    for i in range(new_size): 
        for j in range(new_size): 
            submatrix_a11[i][j] = matrix_a[i][j]
            submatrix_a12[i][j] = matrix_a[i][j + new_size]
            submatrix_a21[i][j] = matrix_a[i + new_size][j]
            submatrix_a22[i][j] = matrix_a[i + new_size][j + new_size]
            submatrix_b11[i][j] = matrix_b[i][j]
            submatrix_b12[i][j] = matrix_b[i][j + new_size]
            submatrix_b21[i][j] = matrix_b[i + new_size][j]
            submatrix_b22[i][j] = matrix_b[i + new_size][j + new_size]   
    
    # Initialise product submatrices
    product_c11 = [[0 for _ in range(new_size)] for _ in range(new_size)]
    product_c11_ = [[0 for _ in range(new_size)] for _ in range(new_size)]
    product_c12 = [[0 for _ in range(new_size)] for _ in range(new_size)]
    product_c12_ = [[0 for _ in range(new_size)] for _ in range(new_size)]
    product_c21 = [[0 for _ in range(new_size)] for _ in range(new_size)]
    product_c21_ = [[0 for _ in range(new_size)] for _ in range(new_size)]
    product_c22 = [[0 for _ in range(new_size)] for _ in range(new_size)]
    product_c22_ = [[0 for _ in range(new_size)] for _ in range(new_size)]
    
    # Recursively call multiply_square_matrix_recursive to compute submatrix products
    multiply_square_matrix_recursive(submatrix_a11, submatrix_b11, product_c11, new_size)
    multiply_square_matrix_recursive(submatrix_a12, submatrix_b21, product_c11_, new_size)
    multiply_square_matrix_recursive(submatrix_a11, submatrix_b12, product_c12, new_size)
    multiply_square_matrix_recursive(submatrix_a12, submatrix_b22, product_c12_, new_size)
    multiply_square_matrix_recursive(submatrix_a21, submatrix_b11, product_c21, new_size)
    multiply_square_matrix_recursive(submatrix_a22, submatrix_b12, product_c21_, new_size)
    multiply_square_matrix_recursive(submatrix_a21, submatrix_b12, product_c22, new_size)
    multiply_square_matrix_recursive(submatrix_a22, submatrix_b22, product_c22_, new_size)
    
    # Combine submatrix results to form the final matrix
    for i in range(new_size):
        for j in range(new_size):
            matrix_c[i][j] = product_c11[i][j] + product_c11_[i][j]
            matrix_c[i][j + new_size] = product_c12[i][j] + product_c12_[i][j]
            matrix_c[i + new_size][j] = product_c21[i][j] + product_c21_[i][j]
            matrix_c[i + new_size][j + new_size] = product_c22[i][j] + product_c22_[i][j]

def multiply_square_matrix_recursive_improved(matrix_a: List[List[int]], matrix_b: List[List[int]]) -> None:
    # Get the size of the matrices
    n = len(matrix_a)
    
    # Base case: if matrices are 1x1, compute their product directly
    if n == 1:
        return [[matrix_a[0][0] * matrix_b[0][0]]]
    
    # Divide step: split matrices A and B into submatrices
    new_size = n // 2
    a11 = [row[:new_size] for row in matrix_a[:new_size]]
    a12 = [row[new_size:] for row in matrix_a[:new_size]]
    a21 = [row[:new_size] for row in matrix_a[new_size:]]
    a22 = [row[new_size:] for row in matrix_a[new_size:]]
    
    b11 = [row[:new_size] for row in matrix_b[:new_size]]
    b12 = [row[new_size:] for row in matrix_b[:new_size]]
    b21 = [row[:new_size] for row in matrix_b[new_size:]]
    b22 = [row[new_size:] for row in matrix_b[new_size:]]
    
    # Recurive calls: compute submatrix products
    c11 = add_square_matrix(
        multiply_square_matrix_recursive_improved(a11, b11), 
        multiply_square_matrix_recursive_improved(a12, b11), 
    )
    c12 = add_square_matrix(
        multiply_square_matrix_recursive_improved(a11, b12),
        multiply_square_matrix_recursive_improved(a12, b22)
    )
    c21 = add_square_matrix(
        multiply_square_matrix_recursive_improved(a21, b11),
        multiply_square_matrix_recursive_improved(a22, b21)
    )
    c22 = add_square_matrix(
        multiply_square_matrix_recursive_improved(a21, b12),
        multiply_square_matrix_recursive_improved(a22, b22)
    )
    
    # Combine step: combine submatrix produxts to compute the final product matrix
    result_matrix = []
    for i in range(new_size):
        result_matrix.append(c11[i] + c12[i])
    for i in range(new_size):
        result_matrix.append(c21[i] + c22[i])
    
    return result_matrix
    
def add_square_matrix(matrix_a: List[List[int]], matrix_b: List[List[int]]) -> List[List[int]]:
    # Add corresponding elements of two matrices
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
    
    
if __name__ == '__main__':
    A = [
        [1, 2],
        [3, 4],
    ]

    B = [
        [1, 2],
        [3, 4],
    ]

    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    multiply_square_matrix_recursive(A, B, C, n)
    
    print('------- Original method -------')
    
    for row in C:
        print(row)
        
    print('------- Improved method -------')
    multiply_square_matrix_recursive_improved(A, B)
    
    for row in C:
        print(row)
        
    # Expected results: 
    # [7, 10]
    # [11, 22]