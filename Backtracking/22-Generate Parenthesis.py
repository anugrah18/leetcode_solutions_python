class Solution:
    def generateParenthesis(self,n):
        ans = []
        def Parenthesis(S='',left=0,right=0):
            if(len(S)==2*n):
                ans.append(S)
            if(left<n):
                Parenthesis(S + '(',left+1,right)
            if(right<left):
                Parenthesis(S + ')', left, right+1)

        Parenthesis()
        return ans

X = Solution()
print(X.generateParenthesis(3))
