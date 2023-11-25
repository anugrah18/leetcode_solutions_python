class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right =right

    # Using recursion.
    def maxDepth(self,root):
        if(root == None):
            return 0
        else:
            lHeight = self.maxDepth(root.left)
            rHeight = self.maxDepth(root.right)
            return max(lHeight,rHeight)+1

    # Using iterations.
    def maxDepth_II(self, root):
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth


tree=  Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)
tree.right.left.left = Node(25)

print(tree.maxDepth(tree))
print(tree.maxDepth_II(tree))

# Time Complexity : O(N)
# Space Complexity : O(N)





