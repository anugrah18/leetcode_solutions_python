class Solution(object):
    def twoSum(self, nums, target):
       h = {}
       for i,num in enumerate(nums):
           n = target-num
           if n not in h:
               h[num] = i
           else:
               return[h[n],i]

x = Solution()
answer = x.twoSum([2, 7, 11, 15],9)
print(answer)


# Time Complexity : O(N)
# Space Complexity : O(N)