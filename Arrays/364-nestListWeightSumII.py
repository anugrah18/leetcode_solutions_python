class Solution:
    def depthSum(self,nestedList):
        def getList(list):
            ans = []
            for lt in list:
                ans.append(lt)
            return ans


        def depth(nestedList):
            curr_depth=1
            for x in nestedList:
                if isinstance(x,int)==False:
                    if getList(x):
                        curr_depth = max(curr_depth,1+depth(getList(x)))
                    else:
                        curr_depth = max(curr_depth, depth(getList(x)))
            return curr_depth

        def dfs(lt,lvl,max_depth):

            ans = 0
            for e in lt:
                if isinstance(e, int):
                    ans += int(e) * (max_depth-lvl+1)
                else:
                    ans += dfs(getList(e), lvl + 1,max_depth)
            return ans

        max_depth = depth(nestedList)
        return dfs(nestedList, 1,max_depth)

X = Solution()
print(X.depthSum([1,[4,[6]]]))

# Time Complexity : O(N)
# Space Complexity : O(N)