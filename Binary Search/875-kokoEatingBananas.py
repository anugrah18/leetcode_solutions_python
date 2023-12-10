import math

class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        # Initialize the search space
        l, r = 1, max(piles)
        # Initialize the result to the maximum possible speed
        res = r

        # Binary search to find the minimum valid speed
        while l <= r:
            # Calculate mid speed
            k = (l + r) // 2
            # Calculate the total hours needed at the current speed
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            # Check if the current speed is sufficient to eat all bananas within h hours
            if hours <= h:
                # If true, update the result and move towards lower speeds
                res = min(res, k)
                r = k - 1
            else:
                # If false, increase the speed
                l = k + 1

        # Return the minimum valid speed found
        return res

X = Solution()
print(X.minEatingSpeed([3,6,7,11],8))

# Time Complexity : O(N log M), where N is the length of the piles list,
# and M is the maximum size of a pile.The binary search has a time complexity
# of log M, and for each iteration, we calculate the total hours needed by iterating through all piles, which takes O(N) time.
# Space Complexity= O(1)