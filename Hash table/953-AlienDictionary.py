class Solution:
    def isAlienSorted(self,words,order):
        ht = {}

        for i in range(0,len(order)):
            ht[order[i]]=i

        for i in range(1,len(words)):
            if(self._comparer(words[i-1],words[i],ht) >0):
                return False

        return True


    def _comparer(self,word1,word2,ht):
        i = 0
        j = 0

        while(i<len(word1) and j<len(word2)):
            if(ht[word1[i]]!=ht[word2[j]]):
                return ht[word1[i]]-ht[word2[j]]
            else:
                i+=1
                j+=1

        return -1 if i==len(word1) else 1

X = Solution()
print(X.isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))

# Time Complexity : O(M) , M = total number of characters in words , N = length of order
# Space Complexity : O(N)