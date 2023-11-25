class Solution:
    def longestConsecutive(self, nums) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                # Iterate through consecutive elements to find the length of the sequence
                while (n + length) in numSet:
                    length += 1
                # Update the maximum sequence length
                longest = max(length, longest)
        return longest

X = Solution()
print(X.longestConsecutive([100,4,200,1,3,2]))

# Time Complexity : O(N)
# Space Complexity : O(N)