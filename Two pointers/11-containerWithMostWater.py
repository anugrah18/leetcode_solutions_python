class Solution:
    def maxArea(self,heights):
        ptr1 = 0
        ptr2 = len(heights)-1
        maxArea = 0

        while(ptr1<ptr2):
            maxArea = max(maxArea,min(heights[ptr1],heights[ptr2])*(ptr2-ptr1))
            if(heights[ptr1]<heights[ptr2]):
                ptr1+=1
            else:
                ptr2-=1

        return maxArea

X = Solution()
print(X.maxArea([1,8,6,2,5,4,8,3,7]))

# Time Complexity : O(N)
# Space Complexity : O(1)