class Solution:
    def combinationSum_I(self, candidates, target):
        res = []

        def dfs(i, curr, total):
            # If the current total equals the target, append a copy of the current combination to the result
            if total == target:
                # shallow copy of curr
                res.append(curr.copy())
                return
            # If the index is out of bounds or the current total exceeds the target, return
            if i >= len(candidates) or total > target:
                return
            # Include the current candidate in the combination
            curr.append(candidates[i])
            # Recur with the current candidate included
            dfs(i, curr, total + candidates[i])
            # Recur with the current candidate included
            curr.pop()
            # Recur with the next candidate
            dfs(i + 1, curr, total)
        # Start the DFS from the first candidate with an empty combination and a total of 0
        dfs(0, [], 0)
        return res

    def combinationSum_II(self, candidates, target):

        result = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # If the remaining target is 0, append a copy of the current combination to the result
                result.append(list(comb))
            elif remain < 0:
                # If the remaining target is negative, return
                return
            for i in range(start, len(candidates)):
                # Include the current candidate in the combination
                comb.append(candidates[i])
                # Recur with the current candidate included
                backtrack(remain - candidates[i], comb, i)
                # Backtrack by removing the last included candidate
                comb.pop()
        # Start the backtracking with the initial target, empty combination, and starting index 0
        backtrack(target, [], 0)
        # Return the final list of combinations
        return result

X = Solution()
print(X.combinationSum_I([2,3,6,7],7))
print(X.combinationSum_II([2,3,6,7],7))

# Time Complexity : O(2^N) , N = Number of candidates
# Space Complexity : O(N)