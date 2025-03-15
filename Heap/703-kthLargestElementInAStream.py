import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.minHeap, self.k = nums, k  # Store k and nums in instance variables
        heapq.heapify(self.minHeap)  # Convert nums into a min-heap in O(n) time

        # Maintain only the k largest elements in the heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # Remove the smallest element to keep size k

    def add(self, val: int):
        heapq.heappush(self.minHeap, val)  # Insert the new value into the heap

        # If heap size exceeds k, remove the smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]  # The kth largest element is always at the root

# Example usage (fixing the incorrect initialization)
X = KthLargest(3, [4, 5, 8, 2])
print(X.add(3))  # Expected output: 4
print(X.add(5))  # Expected output: 5
print(X.add(10)) # Expected output: 5
print(X.add(9))  # Expected output: 8
print(X.add(4))  # Expected output: 8

# Time Complexity : O(n) + O(logK) , O(n) for initializing heap
# Space Complexity : O(k)