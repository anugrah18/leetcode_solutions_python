from collections import deque

class Solution:
    def findBuildings(self, heights):
        if not heights:
            return []

        ans = []

        max_height = -1

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                ans.append(i)
                max_height = heights[i]

        return ans[::-1]

# Example usage
X = Solution()
print(X.findBuildings([4, 2, 3, 1]))

# Time Complexity: O(N), where N is the number of buildings
# Space Complexity: O(N), where N is the number of buildings
