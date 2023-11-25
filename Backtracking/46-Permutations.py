class Solution:
    def permute(self,nums):
        if(len(nums)<2):
            return [nums]
        ans = []

        for i,num in enumerate(nums):
            for permutation in self.permute(nums[0:i]+nums[i+1:]):
                ans.append([num]+permutation)
        return ans

X = Solution()
print(X.permute([1,2,3]))