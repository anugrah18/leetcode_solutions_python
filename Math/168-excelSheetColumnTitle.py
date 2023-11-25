class Solution(object):
    def convertToTitle(self, n):
        ans = ""

        while(n>0):
            n = n-1
            ans = chr(65+ n%26) + ans
            n= n//26

        return ans


X =Solution();
colNum = 701
print(X.convertToTitle(colNum))