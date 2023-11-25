class Solution:
    def findDuplicates(self, nums):
        ans = set()

        for n in nums:
            if nums[abs(n)-1]<0:
                ans.add(abs(n))
            else:
                nums[abs(n)-1]*=-1

        return list(ans)

X = Solution()
print(X.findDuplicates([4,3,2,7,8,2,3,1]))


# Time Complexity : O(N)
# Space Complexity : O(N)