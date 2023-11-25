class Solution(object):

    def lengthOfLongestSubstring(self, s):
        dict = {}
        ans = 0
        i = 0
        j = 0

        while (i < len(s) and j < len(s)):
            if (s[j] not in dict):
                dict[s[j]] = s[j]
                j = j + 1
                ans = max(ans, j - i)
            else:
                dict.pop(s[i])
                i = i + 1
        return ans


X = Solution()
print(X.lengthOfLongestSubstring("xcwxcabcxc"))

# Time Complexity : O(n)
# Space Complexity : O(min(m,n))