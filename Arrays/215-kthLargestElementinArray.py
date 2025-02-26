import heapq
import random

class Solution:
    # Approach I : Using Quick select
    # Time Complexity : O(N) in average case but O(N^2) in worst case
    # Space Complexity : O(N)
    def findKthLargest_I(self, nums, k):
        def quick_select(nums, k):
            # Choose a random pivot to improve average case performance.
            pivot = random.choice(nums)

            # Partition array into three parts.
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            # If k is within the left partition, recurse on the left
            if k <= len(left):
                return quick_select(left, k)
            # If k is beyond left and mid partitions, recurse on the right
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))

            return pivot

        return quick_select(nums, k)


    # Approach II : Using Heap
    # Time Complexity : O(Nlogk)
    # Space Complexity : O(k)
    def findKthLargest_II(self,nums,k):
        return heapq.nlargest(k,nums)[-1]





X = Solution()
print(X.findKthLargest_I([3,2,3,1,2,4,5,5,6],4))
print(X.findKthLargest_II([3,2,3,1,2,4,5,5,6],4))

