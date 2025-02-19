class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def lowestCommonAncestorIII(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Find the lowest common ancestor (LCA) of nodes p and q in a binary tree
        where each node has a parent pointer.
        """
        a, b = p, q

        while a != b:
            # Move up to the parent; if at the root, switch to the other node
            a = a.parent if a else q
            b = b.parent if b else p

        return a  # LCA found


# Example Usage:
# Constructing the following tree:
#        3
#       / \
#      5   1
#     / \   \
#    6   2   8
#       / \
#      7   4

root = Node(3)
node5 = Node(5, parent=root)
node1 = Node(1, parent=root)
node6 = Node(6, parent=node5)
node2 = Node(2, parent=node5)
node8 = Node(8, parent=node1)
node7 = Node(7, parent=node2)
node4 = Node(4, parent=node2)


# Finding LCA
ans = Solution()
print(ans.lowestCommonAncestorIII(node5,node8).val)

# Time Complexity: O(H), where H is the height of tree
# Space Complexity: O(1)
