def rotate(matrix: list[list[int]]):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Rotate the matrix
    for i in range(n):
        for j in range(int(n / 2)):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
    

if __name__ == "__main__":
    m = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    rotate(m)
    
    print(m)
# OUTPUT: [[7,4,1],[8,5,2],[9,6,3]]