class Solution:
    def depthSum(self,nestedList):
        def getList(list):
            ans = []
            for lt in list:
                ans.append(lt)
            return ans


        def dfs(lt,lvl):
            ans = 0
            for e in lt:
                if isinstance(e,int):
                    # If the element is an integer, multiply it by its depth level
                    # and add the result to the accumulated sum.

                    # For leetcode use e.getInteger()
                    ans+=int(e)*lvl
                else:
                    # If the element is a list, recursively call dfs on this list
                    # with an incremented depth level (lvl + 1) and add the result to ans.

                    # For leetcode use e.getList()
                    ans+=dfs(getList(e),lvl+1)
            return ans

        return dfs(nestedList,1)

X = Solution()
print(X.depthSum([1,[4,[6]]]))

# Time Complexity : O(N)
# Space Complexity : O(N)
