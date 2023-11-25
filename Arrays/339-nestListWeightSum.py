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
                    ans+=int(e)*lvl
                else:
                    ans+=dfs(getList(e),lvl+1)
            return ans

        return dfs(nestedList,1)

X = Solution()
print(X.depthSum([1,[4,[6]]]))

# Time Complexity : O(N)
# Space Complexity : O(N)
