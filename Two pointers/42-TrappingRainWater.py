class Solution:
    def trap(self,height):
        # Initialize the left pointer to the first bar
        left =0
        # Initialize the right pointer to the last bar
        right =len(height)-1
        # Variable to store the maximum height encountered from the left side
        left_max =0
        # Variable to store the maximum height encountered from the right side
        right_max =0
        # Variable to store the total trapped water
        ans = 0

        while(left<right):
            # Compare the heights at the left and right pointers
            if(height[left]<height[right]):
                # If height at left is smaller, process the left side
                if(left_max<=height[left]):
                    # Update the maximum height encountered from the left
                    left_max=height[left]
                else:
                    # Add trapped water between the bars
                    ans+=left_max-height[left]
                # Move the left pointer to the next bar
                left+=1
            else:
                # If height at right is smaller or equal, process the right side
                if(right_max<=height[right]):
                    # Update the maximum height encountered from the right
                    right_max = height[right]
                else:
                    # Add trapped water between the bars
                    ans+=right_max-height[right]
                # Move the right pointer to the next bar
                right-=1

        return ans

X = Solution()
print(X.trap([4,2,0,3,2,5]))

# Time Complexity: O(N)
# Space Complexity: O(1)