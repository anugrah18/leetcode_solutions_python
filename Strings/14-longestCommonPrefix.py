class Solution(object):
    def longestCommonPrefix(self,strs):
        if(len(strs)==0):
            return ""

        prefix = strs[0]

        for i in range(0,len(strs)):
            while(strs[i].find(prefix)!=0):
                prefix = prefix[:-1]

        return prefix


X = Solution()
print(X.longestCommonPrefix(["flower","flow","flight"]))


# Time complexity : O(N) , where N is sum of all characters in all strings
# Space complexity : O(1)