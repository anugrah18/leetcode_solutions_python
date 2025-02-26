import random


class Solution:
    def __init__(self, w):
        """
        Initializes the object with an array of weights.

        - Computes the prefix sum array `self.prefix_sums` where each element at index `i`
          is the sum of all weights from index 0 to `i`.
        - Stores the total sum of weights for random sampling.

        Time Complexity: O(N) for pre-processing
        Space Complexity: O(N) for storing prefix sums
        """
        self.prefix_sums = []
        prefix_sum = 0

        # Compute prefix sum array
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)

        self.total_sum = prefix_sum  # Store the total weight sum

    def pickIndex(self):
        """
        Picks an index randomly based on the weight distribution.

        - Generates a random number in the range [0, total_sum).
        - Uses binary search to efficiently find the smallest index where the prefix sum
          is greater than or equal to the target.

        Time Complexity: O(log N) for binary search
        Space Complexity: O(1) (no extra storage except for variables)
        """
        target = self.total_sum * random.random()  # Generate random number in range [0, total_sum)

        # Binary search to find the corresponding weight interval
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = (high + low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1  # Move right
            else:
                high = mid  # Move left
        return low  # The index corresponds to the picked weight interval


# Example Usage
X = Solution([1, 4])  # Weights [1,4] mean index 1 is picked ~80% of the time
print(X.pickIndex())  # Outputs 0 or 1 based on weighted probability


# Time Complexity: O(N) for pre-processing
# Space Complexity: O(N) for storing prefix sums