class Solution:
    def findMin(self, nums) -> int:
        L, R = 0, len(nums) - 1
        res = float('inf')
        while (L <= R):
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break
            mid = L + (R - L) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid - 1

        return res

X= Solution()
print(X.findMin([3,4,5,1,2]))

# Time complexity : O(logN)
# Space complexity : O(1)