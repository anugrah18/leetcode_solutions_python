class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there's only one row, the zigzag conversion doesn't change the string
        if numRows == 1:
            return s

        res = ""  # Resultant string after zigzag conversion

        # Loop through each row in the zigzag pattern
        for r in range(numRows):
            # Calculate the step size to move vertically down the zigzag
            increment = 2 * (numRows - 1)

            # Traverse the string in increments of 'increment'
            for i in range(r, len(s), increment):
                res += s[i]  # Add the current character to the result

                # Handle characters in the middle of the zigzag (not the first or last row)
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]

        return res  # Return the final zigzag converted string

X = Solution()
print(X.convert("PAYPALISHIRING", 3))
# Time Complexity: O(N), N = Length on string
# Space Complexity: O(N)

