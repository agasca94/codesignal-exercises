def maximalSquare(matrix):
    if not matrix:
        return 0 

    rows = len(matrix)
    cols = len(matrix[0])
    sol = 0
    
    for col in reversed(range(cols)):
        for row in reversed(range(rows)):
            if matrix[row][col] == '0':
                s = 0
            elif row == rows - 1 or col == cols - 1:
                s = 1
            else:
                x1 = matrix[row][col + 1]
                x2 = matrix[row + 1][col]
                x3 = matrix[row + 1][col + 1]
                s = min(x1, x2, x3) + 1
            
            matrix[row][col] = s
            if s > sol:
                sol = s
    return sol ** 2