class Solution:
    def isMatch(self, s, p):
        if s == p:
            return True

        row = len(p) + 1
        col = len(s) + 1
        mat = [[False for x in range(col)] for y in range(row)]

        # Empty string matches itself
        mat[0][0] = True

        # Fix the first column
        for i in range(0, len(p)):
            c = p[i]
            if c == "*":
                mat[i + 1][0] = mat[i][0]

        for i in range(len(p)):
            for j in range(len(s)):
                c1 = s[j]
                c2 = p[i]
                if c2 == "*":
                    mat[i + 1][j + 1] = mat[i + 1][j] or mat[i][j + 1]
                elif c2 == "?":
                    mat[i + 1][j + 1] = mat[i][j]
                elif c1 == c2:
                    mat[i + 1][j + 1] = mat[i][j]

        return mat[len(p)][len(s)]

X =Solution()
print(X.isMatch("abcdef","a?c*f"))