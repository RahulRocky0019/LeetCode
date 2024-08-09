class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(matrix, i, j):
            digits = [True] * 10
            for x in range(3):
                for y in range(3):
                    num = matrix[i + x][j + y]
                    if num < 1 or num > 9:
                        return False
                    if digits[num]:
                        digits[num] = False
                    else:
                        return False

            diagonal1 = matrix[i][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 2]
            diagonal2 = matrix[i + 2][j] + matrix[i + 1][j + 1] + matrix[i][j + 2]

            if diagonal1 != diagonal2:
                return False

            row1 = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2]
            row2 = matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2]
            row3 = matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]

            if not (row1 == diagonal1 and row2 == diagonal1 and row3 == diagonal1):
                return False

            col1 = matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j]
            col2 = matrix[i][j + 1] + matrix[i + 1][j + 1] + matrix[i + 2][j + 1]
            col3 = matrix[i][j + 2] + matrix[i + 1][j + 2] + matrix[i + 2][j + 2]

            if not (col1 == diagonal1 and col2 == diagonal1 and col3 == diagonal1):
                return False

            return True
        

        if len(grid) < 3 and (len(grid[0])) < 3:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m - 2):
            for j in range(n - 2):
                if is_magic(grid, i, j):
                    count += 1
            
        return count
