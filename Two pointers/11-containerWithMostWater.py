class Solution:
    def maxArea(self,heights):
        # Initialize the left pointer to the first element of the height list
        ptr1 = 0
        # Initialize the right pointer to the last element of the height list
        ptr2 = len(heights)-1
        maxArea = 0

        while(ptr1<ptr2):
            # Calculate the area between the vertical lines formed by the pointers
            maxArea = max(maxArea,min(heights[ptr1],heights[ptr2])*(ptr2-ptr1))
            # Move the pointers towards each other based on the shorter vertical line
            if(heights[ptr1]<heights[ptr2]):
                ptr1+=1
            else:
                ptr2-=1

        return maxArea

X = Solution()
print(X.maxArea([1,8,6,2,5,4,8,3,7]))

# Time Complexity : O(N)
# Space Complexity : O(1)