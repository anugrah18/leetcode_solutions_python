class Solution:
    # Approach I : Two pointer approach
    # Time Complexity : O(N)
    # Space Complexity : O(1)
    def sortColors_I(self, nums):

        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0 ,len(nums)-1
        i = 0

        while i<=r:
            if nums[i]==0:
                nums[l],nums[i]=nums[i],nums[l]
                l+=1
                i+=1
            elif nums[i]==2:
                nums[r],nums[i]=nums[i],nums[r]
                r-=1
            else:
                i+=1

    # Approach II : Bucket sort approach
    # Time Complexity : O(N)
    # Space Complexity : O(1)
    def sortColors_II(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = {0: 0, 1: 0, 2: 0}
        for num in nums:
            buckets[num] += 1

        last_index = 0
        for val, count in buckets.items():
            current_index = last_index + count
            nums[last_index:current_index] = [val] * (current_index - last_index)
            last_index = current_index

        return nums

X = Solution()
nums1,nums2= [2,0,2,1,1,0],[2,0,2,1,1,0]
X.sortColors_I(nums1)
X.sortColors_I(nums2)
print(nums1)
print(nums2)