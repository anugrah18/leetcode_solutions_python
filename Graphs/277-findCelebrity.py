class Solution:
    def __init__(self):
        # Initialize the relationship matrix where relationship[a][b] indicates
        # whether person 'a' knows person 'b'.
        # 1 means 'a' knows 'b', 0 means 'a' doesn't know 'b'.
        self.relationship = [[1, 1, 0], [0, 1, 0], [1, 1, 1]]

    def knows(self, a, b):
        if self.relationship[a][b] == 1:
            return True
        else:
            return False

    def findCelebrity(self, n):
        # Start with the first person as the celebrity candidate
        celeb_candidate = 0

        # Determine the celebrity candidate
        for i in range(1, n):
            # If the current candidate knows person 'i',
            # then the candidate cannot be a celebrity, update the candidate to 'i'.
            if self.knows(celeb_candidate, i):
                celeb_candidate = i

        # Verify if the candidate is a valid celebrity
        if self.isCeleb(celeb_candidate, n):
            return celeb_candidate
        else:
            return -1

    def isCeleb(self, celeb, n):
        for i in range(n):
            # Skip self-check for the candidate
            if i == celeb:
                continue
            # If the celebrity knows someone, they are not a celebrity
            if self.knows(celeb, i):
                return False
            # If someone doesn't know the celebrity, they are not a celebrity
            if not self.knows(i, celeb):
                return False
        return True


# Example usage:
X = Solution()
print(X.findCelebrity(3))  # Output: 1

# Explanation:
# - Person 1 is the celebrity because:
#   1. Everyone (0 and 2) knows person 1.
#   2. Person 1 doesn't know anyone else.

# Time Complexity: O(N)
# - The initial loop to determine the celebrity candidate runs O(N).
# - The verification loop runs O(N).
# - Total complexity is O(N).

# Space Complexity: O(1)
# - The algorithm uses constant extra space.
