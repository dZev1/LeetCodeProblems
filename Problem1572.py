def diagonalSum(mat: list[list[int]]) -> int:
    length_row_col: int = len(mat[0])
    sum: int = 0
    j: int = 0
    
    for i in range(len(mat)):
        if i == (len(mat) - 1) / 2:
            sum += mat[i][j]
        else:
            sum += mat[i][j] + mat[i] [length_row_col - 1 - j]
        j += 1
    
    return sum

if __name__ == "__main__":
    mat = [[1,1,1,1],
           [1,1,1,1],
           [1,1,1,1],
           [1,1,1,1]]
    print(diagonalSum(mat))
    # OUTPUT = 8
