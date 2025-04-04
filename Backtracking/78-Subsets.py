class Solution:
    def subsets(self, nums):
        res = []  # Final result list to store all subsets
        subset = []  # Temporary list to build each subset

        # Recursive function to explore inclusion/exclusion of each element
        def dfs(i):
            # Base case: if we've considered all elements
            if i >= len(nums):
                res.append(subset.copy())  # Save a copy of the current subset
                return

            # Include nums[i] in the subset
            subset.append(nums[i])
            dfs(i + 1)  # Recurse with element included

            # Backtrack: remove nums[i] and try the path where it's excluded
            subset.pop()
            dfs(i + 1)  # Recurse with element excluded

        dfs(0)  # Start DFS from the first index
        return res  # Return all generated subsets


X = Solution()
print(X.subsets([1, 2, 3]))

# Time Complexity : O(n*2^n)
# Space Complexity : O(2^n)
