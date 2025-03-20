class Solution:
    def longestConsecutive(self, nums):
        # Initialize the longest streak counter
        longest_streak = 0

        # Convert the list to a set for O(1) average-time lookups
        num_set = set(nums)

        # Iterate through each number in the set
        for num in num_set:
            # Check if it's the start of a new sequence (i.e., num-1 is not in set)
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Continue counting the streak while the next number is in the set
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the maximum streak found
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
X = Solution()
print(X.longestConsecutive([100,4,200,1,3,2]))

# Time Complexity : O(N)
# Space Complexity : O(N)