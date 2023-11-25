import heapq

class Solution:
    # Approach I : Using Heap
    # Time Complexity : O(Nlogk)
    # Space Complexity : O(k)
    def findKthLargest_I(self,nums,k):
        return heapq.nlargest(k,nums)[-1]

    # Approach II : Using Quick select
    # Time Complexity : O(N) in average case but O(N^2) in worst case
    # Space Complexity : O(1)
    def findKthLargest_II(self,nums,k):
        k =len(nums)-k

        def quickSelect(l,r):
            pivot , p = nums[r],l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p],nums[i] = nums[i],nums[p]
                    p+=1
            nums[p],nums[r] = nums[r],nums[p]

            if p > k:
                return quickSelect(l,p-1)
            elif p<k:
                return quickSelect(p+1,r)
            else:
                return nums[p]
        return quickSelect(0,len(nums)-1)








X = Solution()
print(X.findKthLargest_I([3,2,3,1,2,4,5,5,6],4))
print(X.findKthLargest_II([3,2,3,1,2,4,5,5,6],4))

