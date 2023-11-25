class Solution(object):
    def isAnagram(self, s, t):

        dict = [0] * 256

        for c in s:
            dict[ord(c)] = dict[ord(c)]+1

        for c in t:
            dict[ord(c)] = dict[ord(c)]-1

        for d in dict:
            if (d!=0):
                return False

        return True


x = Solution()
print(x.isAnagram('god','dog'))

# Time Complexity : O(N)
# Space Complexity : O(1)




