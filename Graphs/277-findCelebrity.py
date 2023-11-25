class Solution:
    def __init__(self):
        self.relationship = [[1,1,0],[0,1,0],[1,1,1]]
    def knows(self, a, b):
        if self.relationship[a][b]==1:
            return True
        else:
            return False

    def findCelebrity(self,n):
        celeb_candidate = 0
        for i in range(1,n):
            if self.knows(celeb_candidate,i):
                celeb_candidate=i

        if self.isCeleb(celeb_candidate,n):
            return celeb_candidate
        else:
            return -1


    def isCeleb(self,celeb,n):
        for i in range(n):
            if i==celeb:
                continue
            if self.knows(celeb,i):
                return False
            if not self.knows(i,celeb):
                return False
        return True

X = Solution()
print(X.findCelebrity(3))

# Time Complexity : O(N)
# Space Complexity : O(1)