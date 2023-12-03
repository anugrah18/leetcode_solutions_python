class MinStack:
    def __init__(self):
        # Initialize an empty stack to store elements along with their minimum values
        self.stack = []

    def push(self, val: int) -> None:
        # If the stack is empty, push the tuple (value, value) onto the stack
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            # If the current value is smaller than the current minimum, push (value, value)
            # Otherwise, push (value, current_minimum)
            if self.stack[-1][1] > val:
                self.stack.append((val, val))
            else:
                self.stack.append((val, self.stack[-1][1]))

    def pop(self) -> None:
        # Pop the top element from the stack
        if len(self.stack) > 0:
            self.stack.pop()

    def top(self) -> int:
        # Return the value of the top element on the stack
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the minimum value stored in the stack
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