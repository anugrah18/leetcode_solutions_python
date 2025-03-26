class Solution:
    def findDiagonalOrder(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        res = []  # Result list to store elements in diagonal order

        cur_row = cur_col = 0  # Start from top-left corner
        going_up = True  # Direction flag: True for upward-right, False for downward-left

        # Continue until all elements are collected
        while len(res) != rows * cols:
            if going_up:
                # Move in upward-right direction
                while cur_row >= 0 and cur_col < cols:
                    res.append(mat[cur_row][cur_col])
                    cur_row -= 1  # Move up
                    cur_col += 1  # Move right

                # Adjust position after exiting loop (out of bounds)
                if cur_col == cols:
                    cur_col -= 1  # Go back into bounds
                    cur_row += 2  # Move down two to start next diagonal
                else:
                    cur_row += 1  # Just step down to continue

                going_up = False  # Switch direction
            else:
                # Move in downward-left direction
                while cur_row < rows and cur_col >= 0:
                    res.append(mat[cur_row][cur_col])
                    cur_row += 1  # Move down
                    cur_col -= 1  # Move left

                # Adjust position after exiting loop (out of bounds)
                if cur_row == rows:
                    cur_row -= 1  # Go back into bounds
                    cur_col += 2  # Move right two to start next diagonal
                else:
                    cur_col += 1  # Just step right to continue

                going_up = True  # Switch direction

        return res


X = Solution()
print(X.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# Time Complexity : O(M*N) , M = num of rows and N = num of cols
# Space Complexity : O(M*N)
