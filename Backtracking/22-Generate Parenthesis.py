class Solution:
    def generateParenthesis(self, n):
        # Initialize an empty list to store generated parentheses combinations
        ans = []

        # Recursive helper function to generate parentheses
        def Parenthesis(S='', left=0, right=0):
            # If the length of the current combination is equal to 2n, add it to the result
            if len(S) == 2 * n:
                ans.append(S)

            # If there are remaining unused left parentheses, add one and recurse
            if left < n:
                Parenthesis(S + '(', left + 1, right)

            # If there are more left parentheses used than right parentheses, add a right parenthesis and recurse
            if right < left:
                Parenthesis(S + ')', left, right + 1)

        # Initial call to the helper function
        Parenthesis()

        # Return the generated combinations
        return ans


X = Solution()
print(X.generateParenthesis(3))

# Time Complexity = O((4^n/sqrt(n)) , where n is the given input n. There are 2n characters
# and four possibiliies
# Space Complexity = O((4^n/sqrt(n)) ,the number of recursive calls is proportional to the
# number of valid combinations generated.
