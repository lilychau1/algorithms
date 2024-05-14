from typing import List
def add_square_matrix(matrix_a: List[List[int]], matrix_b: List[List[int]], matrix_c: List[List[int]], n: int):    
    for i in range(n):
        for j in range(n): 
            matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]

if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    add_square_matrix(A, B, C, n)
    
    for row in C:
        print(row)
        
    # Expected results: 
    # [10, 10, 10]
    # [10, 10, 10]
    # [10, 10, 10]