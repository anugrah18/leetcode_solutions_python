class Solution(object):
    def longestStrChain(self,words):
        words = sorted(words,key=len)
        maxLength = 0
        dict = {}

        for word in words:
            currWord = word
            currBest = 0
            for j in range(0,len(word)):
                pred = word[0:j] + word[j+1:len(word)]
                currBest = max(currBest,dict[pred]+1 if pred in dict else 1)
            dict[currWord] = currBest
            maxLength = max(currBest,maxLength)

        return maxLength

strCollection = ["a","b","ba","bca","bda","bdca","fkbdca","fbdca"]
X = Solution()
print(X.longestStrChain(strCollection))

# Time Complexity = O(NLogN) + O(NL) = O(N(LogN + L)) , N = number of words , L = length of longest word
# Space Complexity = O(N)