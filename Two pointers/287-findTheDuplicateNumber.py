class Solution:
    def findDuplicate(self, nums) -> int:
        # Initialize two pointers, slow and fast, both starting at the first index (0).
        slow, fast = 0, 0

        # Phase 1: Detect a cycle in the list.
        while True:
            slow = nums[slow]           # Move slow pointer by 1 step.
            fast = nums[nums[fast]]     # Move fast pointer by 2 steps.
            if slow == fast:            # If slow and fast meet, a cycle is detected.
                break

        # Phase 2: Find the entry point of the cycle, which is the duplicate number.
        slow2 = 0
        while True:
            slow = nums[slow]           # Move slow pointer by 1 step.
            slow2 = nums[slow2]         # Move slow2 pointer by 1 step from the start.
            if slow == slow2:           # When they meet, the entry point of the cycle is found.
                return slow             # This is the duplicate number.


X = Solution()
print(X.findDuplicate([1,3,4,2,2]))

# Time Complexity : O(N)
# Space Complexity : O(1)
