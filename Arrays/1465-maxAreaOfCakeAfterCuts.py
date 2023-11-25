class Solution:
    def maxArea(self,h,w,horizontalCuts,verticalCuts):
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)

        horizontalCuts.sort()
        verticalCuts.sort()

        h_diff = -1
        w_diff =-1

        for i in range(1,len(horizontalCuts)):
            h_diff = max(h_diff,horizontalCuts[i]-horizontalCuts[i-1])

        for i in range(1,len(verticalCuts)):
            w_diff = max(w_diff,verticalCuts[i]-verticalCuts[i-1])

        return (h_diff*w_diff)%(1000000007)

X = Solution()
print(X.maxArea(5,4,[1,2,4],[1,3]))

# Time Complexity : O(Nlog(N) + Mlog(M))
# Space complexity : O(1)

