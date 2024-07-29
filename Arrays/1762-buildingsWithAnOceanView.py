from collections import deque

class Solution:
    def findBuildings(self, heights):
        if not heights:
            return []

        max_height = -1
        res = deque()  # Use a deque to efficiently append to the left

        # Traverse the list from the end to the beginning
        for i in range(len(heights) - 1, -1, -1):
            cur_height = heights[i]
            # If the current building's height is greater than the maximum height seen so far
            if cur_height > max_height:
                res.appendleft(i)  # Add the building index to the front of the deque
                max_height = cur_height  # Update the maximum height

        return list(res)  # Convert deque to list before returning

# Example usage
X = Solution()
print(X.findBuildings([4, 2, 3, 1]))

# Time Complexity: O(N), where N is the number of buildings
# Space Complexity: O(N), where N is the number of buildings
