class Solution:
    def combinationSum2(self, candidates, target):
        res = []

        # Sort the candidates to easily handle duplicates
        candidates.sort()

        # Depth-first search helper function
        def dfs(i, cur, total):
            # Base case: if the running total equals target, add current combination to result
            if total == target:
                res.append(cur.copy())
                return
            # If the total exceeds target or we've gone past the list, stop
            if total > target or i == len(candidates):
                return

                # Include the current candidate and move to the next index
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()  # backtrack

            # Skip duplicates: advance i until the next distinct number
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            # Exclude the current candidate and move forward
            dfs(i + 1, cur, total)

        # Start DFS from index 0 with empty combination and total = 0
        dfs(0, [], 0)
        return res

# Time Complexity : O(N* 2^N) , There are 2^n subsets in total and we spend , copying array can take n times
# Space Complexity : O(N)
