class Solution:
    def largestRectangleArea(self, heights) -> int:
        maxArea = 0  # Variable to store the maximum rectangle area
        stack = []   # Stack to keep track of indices and heights

        # Iterate through each index and height in the input list
        for i, h in enumerate(heights):
            start = i  # Initialize the starting index

            # While the stack is not empty and the height at the top of the stack is greater than the current height
            while stack and stack[-1][1] > h:
                index, height = stack.pop()  # Pop the top element from the stack
                maxArea = max(maxArea, height * (i - index))  # Calculate and update the maximum area
                start = index  # Update the starting index to the popped index

            stack.append((start, h))  # Push the current index and height onto the stack

        # Process the remaining elements in the stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

X = Solution()
print(X.largestRectangleArea([2, 1, 5, 6, 2, 3]))

# Time Complexity : O(N)
# Space Complexity : O(N)