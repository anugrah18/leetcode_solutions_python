class Solution:
    def combinationSum_I(self, candidates, target):
        res = []

        def dfs(i, curr, total):
            if total == target:
                # shallow copy of curr
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res

    def combinationSum_II(self, candidates, target):

        result = []

        def backtrack(remain, comb, start):
            if remain == 0:
                result.append(list(comb))
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)

                comb.pop()

        backtrack(target, [], 0)
        return result

X = Solution()
print(X.combinationSum_I([2,3,6,7],7))
print(X.combinationSum_II([2,3,6,7],7))