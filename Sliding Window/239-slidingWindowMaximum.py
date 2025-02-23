import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        # List to store the maximum elements in each sliding window
        output = []

        # Deque to maintain indices of elements in the current window
        q = collections.deque()
        # Pointers for the left (l) and right (r) boundaries of the current window
        l = r = 0

        # Iterate through the array
        while r < len(nums):
            # Remove elements from the back of the deque that are smaller than the
            # current element
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Add the current index to the deque
            q.append(r)

            # Remove the front index of the deque if it is outside the current window
            if l > q[0]:
                q.popleft()

            # If the window size is reached, append the maximum element to the output
            if (r + 1) >= k:
                output.append(nums[q[0]])
                # Move the window forward by incrementing the left pointer
                l += 1
            # Move the right pointer forward
            r += 1

        # Return the list of maximum elements in each sliding window
        return output

X = Solution()
print(X.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))

# Time complexity : O(N)
# Space complexity : O(N)







