class Solution(object):
    def isValid(self, s):

        # Initialize an empty stack to track opening parentheses
        stack = []
        # Dictionary to store the mappings of closing and opening parentheses
        Dict = {')': '(', '}': '{', ']': '['}

        # Iterate through each character in the input string
        for c in s:
            # Check if the stack is not empty, the current character is a closing parenthesis,
            # and the corresponding opening parenthesis matches the top of the stack
            if len(stack) > 0 and Dict.get(c) and Dict[c] == stack[len(stack)-1]:
                # Pop the top element from the stack (matching pair found)
                stack.pop()
            else:
                # Push the current character onto the stack
                stack.append(c)

        # If the stack is empty, all parentheses are matched
        return len(stack)==0

X = Solution()
print(X.isValid("{(){}[]}"))

# Time Complexity : O(N)
# Space Complexity : O(N)
