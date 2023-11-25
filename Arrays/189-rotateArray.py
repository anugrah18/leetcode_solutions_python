class Solution(object):


    def rotate_I(self,nums,k):


        def reverse(nums: list, start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        n = len(nums)
        k %= n

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
        return nums

    def rotate_II(self, nums, k):

        k = k% len(nums)
        nums[k:],nums[:k] = nums[:-k],nums[-k:]

        return nums

X =Solution()
print(X.rotate_I([1,2,3,4,5,6,7],4))
print(X.rotate_II([1,2,3,4,5,6,7],4))

# Time Complexity : O(N)
# Space Complexity : O(1)