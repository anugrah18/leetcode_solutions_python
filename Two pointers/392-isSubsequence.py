class Solution:
    def isSubsequence(self, s, t):
        left, right = len(s), len(t)

        l_ptr = r_ptr = 0

        while l_ptr < left and r_ptr < right:
            if s[l_ptr] == t[r_ptr]:
                l_ptr += 1
            r_ptr += 1

        return l_ptr == left


X = Solution()
print(X.isSubsequence("abc","ahbgdc"))