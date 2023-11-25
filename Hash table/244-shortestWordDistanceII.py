class WordDistance:
    def __init__(self,words):
        self.dic = {}
        for i,w in enumerate(words):
            self.dic[w] = self.dic.get(w,[])+[i]


    def shortest(self,word1,word2):
        l1,l2 = self.dic[word1],self.dic[word2]
        i = j = 0

        res = float('inf')

        while i<len(l1) and j<len(l2):
            res = min(res,abs(l1[i]-l2[j]))
            if l1[i]<l2[j]:
                i+=1
            else:
                j+=1

        return res

X = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print(X.shortest("coding", "practice"))
print(X.shortest("makes","coding"))

# Time Complexity : O(N)
# Space Complexity : O(N)