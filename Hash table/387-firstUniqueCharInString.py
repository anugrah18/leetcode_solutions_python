class Solution(object):
    def firstUniqChar(self, s):

        dict = {}
        for c in s:
            if(c not in dict):
                dict[c]=1
            else:
                dict[c]=dict[c]+1

        for i in range(0,len(s)):
            if(dict[s[i]]==1):
                return i

        return -1

X = Solution()
print(X.firstUniqChar("leetcode"))

# Time Complexity : O(N)
# Space Complexity : O(N)

