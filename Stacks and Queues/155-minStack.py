class MinStack:
    def __init__(self):
        # Initialize an empty stack. Each element will be a pair: [value, current_min]
        self.stack = []

    def push(self, val: int) -> None:
        # Push the value along with the current minimum
        if self.stack:
            # Compare the new value with the current minimum and store the smaller one
            self.stack.append([val, min(val, self.stack[-1][1])])
        else:
            # If the stack is empty, the value is the current minimum
            self.stack.append([val, val])

    def pop(self) -> None:
        # Remove the top element from the stack
        self.stack.pop()

    def top(self) -> int:
        # Return the top value (not the minimum)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the current minimum value
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Time Complexity : O(1)
# Space Complexity : O(N)