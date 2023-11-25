class Solution:
    def firstMissingPositive(self, nums) -> int:
        # Replacing negatives with zero
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                # Mark as seen
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                # Edge case
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            # Number never showed in list
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1

X = Solution()
print(X.firstMissingPositive([1,2,0]))