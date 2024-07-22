class BinaryMatrix(object):
    def __init__(self, mat):
        self.mat = mat

    def get(self, row: int, col: int) -> int:
        return self.mat[row][col]

    def dimensions(self) -> list:
        return [len(self.mat), len(self.mat[0])]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # Get the dimensions of the matrix
        rows, cols = binaryMatrix.dimensions()

        # Start from the top-right corner of the matrix
        current_row = 0
        current_col = cols - 1

        # Variable to store the result, initialized to -1
        result = -1

        # Traverse the matrix
        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 1:
                # If a '1' is found, update result and move left
                result = current_col
                current_col -= 1
            else:
                # If a '0' is found, move down
                current_row += 1

        return result

# Example usage:
mat = [[0, 0], [1, 1]]
binaryMatrix = BinaryMatrix(mat)
X = Solution()
result = X.leftMostColumnWithOne(binaryMatrix)
print(result)

# Time Complexity : O(rows + cols)
# Space Complexity : O(1)

