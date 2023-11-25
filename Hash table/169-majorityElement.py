class Solution(object):
    def majorityElement(self, nums):
        size = len(nums)

        if (size < 2):
            return nums[0]
        dict = {}

        for num in nums:
            if (num not in dict):
                dict[num] = 1
            else:
                dict[num] = dict[num] + 1
                if (dict[num] > int(size / 2)):
                    return num


X =Solution()
seq = [2,2,1,1,1,2,2]
print(X.majorityElement(seq))

# Time Complexity = O(N)
# Space Complexity = O(N)