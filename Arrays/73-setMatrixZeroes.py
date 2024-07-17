class Solution:
    def setZeroes(self, matrix):
        # Get the number of rows and columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        # Flag to indicate if the first row needs to be set to zero
        rowZero = False

        # First pass: determine which rows and columns need to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # Set the first element of the column to 0
                    matrix[0][c] = 0
                    if r > 0:
                        # Set the first element of the row to 0
                        matrix[r][0] = 0
                    else:
                        # If the zero is in the first row, set the flag
                        rowZero = True

        # Second pass: use the first row and column as markers to set elements to zero
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # If the first element of the matrix is 0, set the first column to zero
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # If the flag is set, set the first row to zero
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0


X = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix)
print(X.setZeroes(matrix))
print(matrix)

# Time Complexity : O(MXN)
# Space Complexity : O(1)