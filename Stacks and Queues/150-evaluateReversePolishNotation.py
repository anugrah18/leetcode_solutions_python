class Solution:
    def evalRPN(self, tokens) -> int:
        # Initialize an empty stack to store operands
        stack = []

        # Iterate through each token in the input list of tokens
        for c in tokens:
            # Check if the current token is an operator
            if c == "+":
                # If it's addition, pop the top two elements from the stack,
                # perform the addition, and push the result back onto the stack
                a, b = stack.pop(), stack.pop()
                stack.append(b + a)
            elif c == "-":
                # If it's subtraction, pop the top two elements, perform the
                # subtraction, and push the result back onto the stack
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                # If it's multiplication, pop the top two elements, perform the
                # multiplication, and push the result back onto the stack
                a, b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif c == "/":
                # If it's division, pop the top two elements, perform the
                # division, and push the result (integer division) back onto the stack
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                # If it's a number, convert it to an integer and push it onto the stack
                stack.append(int(c))

        # The final result is the only element left on the stack
        return stack[0]


X = Solution()
print(X.evalRPN( ["2","1","+","3","*"]))

# Time Complexity : O(N)
# Space Complexity : O(M) M = number of non-operators values