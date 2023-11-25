class Solution(object):
    def reverseString(self, s):
        size = len(s)
        for i in range(0 , int(len(s)/2)):
            s[i],s[size-i-1] = s[size-i-1],s[i]


str = ['a','b','c','d','e']
X = Solution()
print(str)
X.reverseString(str)
print(str)

# Time Complexity : O(N)
# Space Complexity : O(1)




