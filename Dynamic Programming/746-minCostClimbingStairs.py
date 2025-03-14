class Solution:
    def minCostClimbingStairs(self, cost):
        # Append a zero at the end, representing the top of the stairs with no cost
        cost.append(0)

        # Traverse the cost array from the second last step down to the first step
        for i in range(len(cost) - 3, -1, -1):
            # At each step, choose the minimum cost between taking one step or two steps
            cost[i] += min(cost[i + 1], cost[i + 2])

        # The result is the minimum cost of starting at either step 0 or step 1
        return min(cost[0], cost[1])


# Example usage
X = Solution()
print(X.minCostClimbingStairs([10, 15, 20]))

# Time Complexity : O(N)
# Space Complexity : O(1)
