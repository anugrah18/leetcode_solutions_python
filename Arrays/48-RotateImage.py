class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N):
            for j in range(i + 1, N):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(N):
            matrix[i] = (matrix[i][::-1])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
X = Solution()
print(matrix)
X.rotate(matrix)
print(matrix)

# Time Complexity : O(MXN)
# Space Complexity : O(1)