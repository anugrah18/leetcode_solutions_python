# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        if (len(nums) == 0):
            return None
        return self.convertArrayToBST(nums, 0, (len(nums) - 1))

    def convertArrayToBST(self, nums, left, right):
        if (left > right):
            return None
        mid = left + int((right - left) / 2)
        node = TreeNode(nums[mid])
        node.left = self.convertArrayToBST(nums, left, mid - 1)
        node.right = self.convertArrayToBST(nums, mid + 1, right)
        return node


X = Solution()
Tree = X.sortedArrayToBST([1,2,3,4,5])
print(Tree.val)

# Time Complexity : O(N)
# Space Complexity : O(logN)