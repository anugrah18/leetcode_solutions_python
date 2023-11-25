class Solution:
    def containsDuplicate(self, nums) -> bool:
        ht = {}

        for num in nums:
            if num in ht:
                return True
            ht[num] = num

        return False

X = Solution()
print(X.containsDuplicate([1,2,3,1,4]))

# Time Complexity : O(N)
# Space Complexity : O(N)