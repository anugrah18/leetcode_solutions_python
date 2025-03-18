import heapq


class Solution:
    def kClosest(self, points, k: int):

        minHeap = []  # Min heap to store (distance, x, y) tuples

        # Calculate Euclidean distance squared and store in the heap
        for x, y in points:
            dist = (x ** 2) + (y ** 2)  # Squared distance to avoid sqrt computation
            minHeap.append([dist, x, y])  # Store distance along with point coordinates

        # Convert the list into a heap (O(n) operation)
        heapq.heapify(minHeap)

        res = []  # Result list to store k closest points

        # Extract the k smallest elements from the heap
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)  # Pop the smallest distance element
            res.append([x, y])  # Add the point to the result list
            k -= 1  # Decrement k

        return res  # Return the k closest points


# Example usage
X = Solution()
print(X.kClosest([[3, 3], [5, -1], [-2, 4]], 2))  # Expected output: [[3,3], [-2,4]]

# Time Complexity : O(NlogN)
# Space Complexity : O(N)
