from typing import List
def multiply_square_matrix(matrix_a: List[List[int]], matrix_b: List[List[int]], matrix_c: List[List[int]], n: int):    
    """Multiply two square matrices A and B and store the result in matrix C.

    Parameters:
        matrix_a: The first input matrix (size n x n).
        matrix_b: The second input matrix (size n x n).
        matrix_c: The output matrix where the result will be stored (size n x n).
        n: The size of the square matrices.

    Explanation:
        This function computes the element-wise multiplication of square matrices A and B using three nested loops.
        The outer loops iterate over each row index (a_row) and column index (b_col) of the resulting matrix C.
        The innermost loop iterates over the common index (k) used for the dot product calculation.
        For each iteration, the dot product of the k-th row of matrix A and the k-th column of matrix B is computed
        and added to the corresponding element of matrix C.
    """
    # Calculate dot product of a_row and b_col with k as counter to loop through all elemeents in the matrix A row and matrix B column in each calculation
    for a_row in range(n):
        for b_col in range(n): 
            for k in range(n): 
                matrix_c[a_row][b_col] = matrix_c[a_row][b_col] + matrix_a[a_row][k] * matrix_b[k][b_col]

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

    multiply_square_matrix(A, B, C, n)
    
    for row in C:
        print(row)
    
    # Expected results: 
    # [7, 10]
    # [11, 22]