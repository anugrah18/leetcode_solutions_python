class Solution:
    def checkValidString(self, s: str) -> bool:
        # Initialize the range of possible open parentheses counts
        leftMin, leftMax = 0, 0  # min and max number of open '(' possible at current position

        for c in s:
            if c == "(":
                # An open parenthesis increases both min and max count
                leftMin += 1
                leftMax += 1
            elif c == ")":
                # A closing parenthesis decreases both min and max count
                leftMin -= 1
                leftMax -= 1
            else:
                # A '*' can be either '(', ')' or empty
                # So min decreases (if '*' is ')') and max increases (if '*' is '(')
                leftMin -= 1
                leftMax += 1

            # If max goes below 0, too many ')' — invalid
            if leftMax < 0:
                return False

            # If min goes below 0, reset to 0 (we can ignore unmatched ')' so far)
            # because '*' could be treated as empty or '('
            if leftMin < 0:
                leftMin = 0

        # After parsing all characters, if min is 0, all parentheses are matched
        return leftMin == 0


X = Solution()
print(X.checkValidString("(*))"))

# Time Complexity : O(N)
# Space Complexity : O(1)