class Solution:
    def generate(self, numRows):
        # Initialize the result with the first row
        res = [[1]]

        # Generate each row of Pascal's Triangle
        for i in range(numRows - 1):
            # Create a temporary list with a leading and trailing zero
            temp = [0] + res[-1] + [0]
            row = []
            # Generate the next row by summing adjacent elements in the temp list
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            # Append the newly generated row to the result
            res.append(row)

        return res

X = Solution()
print(X.generate((5)))

# Time Complexity : O(N*N)
# Space Complexity : O(N*N)