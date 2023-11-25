class Solution:
    def search(self, nums, target):

        def binarySearch(nums, i, j, target):
            mid = i + (j - i) // 2
            if i > j:
                return -1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(nums, i, mid - 1, target)
            else:
                return binarySearch(nums, mid + 1, j, target)

        return binarySearch(nums, 0, len(nums) - 1, target)

X = Solution()
print(X.search([-1,0,3,5,9,12],9))

# Time Complexity : O(logN)
# Space Complexity : O(1)