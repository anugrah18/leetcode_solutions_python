class Solution:
    def searchMatrix(self, matrix, target):
        # Get the number of rows and columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # Binary search on rows to narrow down the possible row
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        # If top is not less than or equal to bottom, target is not in the matrix
        if not (top <= bottom):
            return False

        # Binary search on the selected row to find the target
        row = (top + bottom) // 2
        left, right = 0, COLS - 1

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        # Target not found in the matrix
        return False


X = Solution()
print(X.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))

# Time Complexity : O(log(rows) + log(cols))
# Space Complexity : O(1)