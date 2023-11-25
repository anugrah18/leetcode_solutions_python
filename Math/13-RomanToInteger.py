class Solution(object):
    def romanToInt(self, s):
        dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        i = 0
        while(i< len(s)):
            if i+1<len(s) and dict[s[i]]<dict[s[i+1]]:
                total = total + dict[s[i+1]] - dict[s[i]]
                i=i+2
            else:
                total = total + dict[s[i]]
                i=i+1

        return total



X = Solution()
print(X.romanToInt("XVIII"))


