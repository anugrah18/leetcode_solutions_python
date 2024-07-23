class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list, verticalCuts: list) -> int:
        # Add the edges of the cake to the cuts list
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)

        # Sort the cuts to find the maximum differences
        horizontalCuts.sort()
        verticalCuts.sort()

        # Initialize variables to store the maximum differences
        h_diff = -1
        w_diff = -1

        # Find the maximum difference between consecutive horizontal cuts
        for i in range(1, len(horizontalCuts)):
            h_diff = max(h_diff, horizontalCuts[i] - horizontalCuts[i-1])

        # Find the maximum difference between consecutive vertical cuts
        for i in range(1, len(verticalCuts)):
            w_diff = max(w_diff, verticalCuts[i] - verticalCuts[i-1])

        # Calculate the maximum area and return it modulo 10^9 + 7
        return (h_diff * w_diff) % (1000000007)

X = Solution()
print(X.maxArea(5,4,[1,2,4],[1,3]))

# Time Complexity : O(Nlog(N) + Mlog(M))
# Space complexity : O(1)

