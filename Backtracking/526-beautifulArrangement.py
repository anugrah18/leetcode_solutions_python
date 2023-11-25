class Solution:
    count = 0
    def countArrangement(self,n):
        visited = [False]*(n+1)
        self.calculatePermutation(n,1,visited)
        return self.count

    def calculatePermutation(self,N,pos,visited):
        if pos>N:
            self.count+=1
        for i in range(1,N+1):
            if (not visited[i] and (pos%i==0 or i%pos==0)):
                visited[i]= True
                self.calculatePermutation(N,pos+1,visited)
                visited[i]=False

X = Solution()
print(X.countArrangement(2))