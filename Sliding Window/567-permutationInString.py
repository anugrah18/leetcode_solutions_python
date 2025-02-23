class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Check if the length of s1 is greater than the length of s2
        if len(s1) > len(s2):
            return False

        # Arrays to store the count of characters in s1 and the current window in s2
        s1Count, s2Count = [0] * 26, [0] * 26

        # Initialize the count arrays for the first window of size len(s1)
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Variable to count the matches between the two count arrays
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        # Iterate through the rest of the string s2 using a sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            # Check if the counts match for all characters
            if matches == 26:
                return True

            # Update the count array for the new character in the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            # Update the matches count based on the new character
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove the count of the character going out of the window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            # Update the matches count based on the character going out of the window
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            # Move the window forward
            l += 1

        # Check for the last window
        return matches == 26


X= Solution()
print(X.checkInclusion( "ab","eidbaooo"))

# Time complexity : O(N)
# Space complexity : O(1)
