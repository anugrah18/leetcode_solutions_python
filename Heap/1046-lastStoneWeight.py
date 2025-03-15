import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Convert all stone weights to negative to use a min-heap as a max-heap
        for i in range(len(stones)):
            stones[i] *= -1  # Negate values to simulate max-heap behavior

        # Transform the list into a heap (min-heap with negated values simulates max-heap)
        heapq.heapify(stones)  # O(n) complexity

        # Process the two largest elements until one or no stone remains
        while len(stones) > 1:
            first = heapq.heappop(stones)  # Extract the heaviest stone (most negative value) -> O(log n)
            second = heapq.heappop(stones)  # Extract the second heaviest stone -> O(log n)

            if second > first:  # If they are not equal, push the remaining weight back
                heapq.heappush(stones, first - second)  # Push the difference (still negative) -> O(log n)

        # If no stones remain, return 0; otherwise, return the last remaining stone's weight
        stones.append(0)  # Ensures there's always an element in the list
        return abs(stones[0])  # Convert back to positive before returning


# Example usage:
X = Solution()
print(X.lastStoneWeight([2, 7, 4, 1, 8, 1]))  # Expected output: 1

# Time Complexity : O(NLogN)
# Space Complexity : O(N)