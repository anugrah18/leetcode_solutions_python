class Solution:
    def spiralOrder(self, matrix) :
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get every i in right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # for single row or column case
            if not left < right or not top < bottom:
                break

            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # get every in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

X = Solution()
print(X.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

# Time Complexity : O(N)
# Space Complexity : O(1)