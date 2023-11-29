class Solution(object):

    def lengthOfLongestSubstring(self, s):
        # Dictionary to store characters and their indices in the current substring
        dict = {}
        ans = 0
        # Pointers to track the start (i) and end (j) of the current substring
        i = 0
        j = 0

        # Iterate through the string using two pointers
        while (i < len(s) and j < len(s)):
            # If the current character is not in the dictionary, add it and move the end pointer (j) forward
            if (s[j] not in dict):
                dict[s[j]] = s[j]
                j = j + 1
                # Update the length of the current substring if it is longer than the previous maximum
                ans = max(ans, j - i)
            else:
                # If the current character is in the dictionary, remove the character at the start pointer (i)
                dict.pop(s[i])
                i = i + 1
        return ans


X = Solution()
print(X.lengthOfLongestSubstring("xcwxcabcxc"))

# Time Complexity : O(n)
# Space Complexity : O(min(m,n)) where n is length of input string s and m in number of distict characters.