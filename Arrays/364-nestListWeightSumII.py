class Solution:
    def depthSum(self, nestedList):
        # Helper function to extract list elements (not needed for LeetCode's interface)
        def getList(lst):
            ans = []
            for lt in lst:
                ans.append(lt)
            return ans

        # Helper function to determine the maximum depth of the nested list
        def depth(nestedList):
            curr_depth = 1
            for x in nestedList:
                # For leetcode use e.isInteger()
                if not isinstance(x, int):
                    # If x is a list, recursively find the maximum depth of the list
                    # For LeetCode, use x.getList()
                    if getList(x):
                        curr_depth = max(curr_depth, 1 + depth(getList(x)))
                    else:
                        curr_depth = max(curr_depth, depth(getList(x)))
            return curr_depth

        # Depth-first search function to calculate weighted sum based on depth
        def dfs(lt, lvl, max_depth):
            ans = 0
            for e in lt:
                # For leetcode use e.isInteger()
                if isinstance(e, int):
                    # If the element is an integer, multiply it by the weight based on its depth
                    # For LeetCode, use e.getInteger()
                    ans += int(e) * (max_depth - lvl + 1)
                else:
                    # If the element is a list, recursively call dfs on this list
                    # with an incremented depth level (lvl + 1) and add the result to ans.
                    # For LeetCode, use e.getList()
                    ans += dfs(getList(e), lvl + 1, max_depth)
            return ans

        # Determine the maximum depth of the nested list
        max_depth = depth(nestedList)
        # Initiate DFS with the initial level set to 1 and the maximum depth
        return dfs(nestedList, 1, max_depth)

# Example usage
X = Solution()
print(X.depthSum([1, [4, [6]]]))

# Time Complexity : O(N)
# Space Complexity : O(N)
