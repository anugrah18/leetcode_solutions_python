class Solution(object):
    def productExceptSelfInThreePasses(self, nums):
        L_To_R = [1] * len(nums)
        R_To_L = [1] * len(nums)
        answer = [0] * len(nums)

        # Calculate left products
        left_product =1
        for i in range(0, len(nums)):
            L_To_R[i] = left_product
            left_product *= nums[i]

        # Calculate right products
        right_product = 1
        for j in range(len(nums) - 1, -1, -1):
            R_To_L[j] =  right_product
            right_product *= nums[j]

        # Calculate the final result
        for i in range(0, len(nums)):
            answer[i] = L_To_R[i] * R_To_L[i]

        return answer

    def productExceptSelfInTwoPasses(self,nums):
        L_To_R = [1] * len(nums)

        # Calculate left products
        left_product= 1
        for i in range(0, len(nums)):
            L_To_R[i] = left_product
            left_product *= nums[i]

        # Initialize a variable to store the product of all elements to the right
        right_product = 1
        # Update the result array in-place by multiplying with the product of all elements to the right
        for i in range(len(nums) - 1, -1, -1):
            L_To_R[i] *= right_product
            right_product *= nums[i]

        return L_To_R




X = Solution()
print(X.productExceptSelfInThreePasses([1, 2, 3, 4, 5]))
print(X.productExceptSelfInTwoPasses([1, 2, 3, 4, 5]))

# Time Complexity : O(N)
# Space Complexity : O(N)