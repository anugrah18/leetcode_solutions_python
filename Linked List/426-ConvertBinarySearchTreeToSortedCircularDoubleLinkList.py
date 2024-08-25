class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # In-place conversion of Binary Search Tree to a circular doubly linked list
    def treeToDoublyListInPlace(self,root: Node) -> Node:
        # In place solution.
        # Time Complexity : O(N)
        # Space Complexity : O(1)
        if not root:
            return
        def dfs(node):
            # Use nonlocal to modify head and tail defined in the outer function.
            nonlocal head,tail
            if not node:
                return
            # In-order traversal: left, node, right
            dfs(node.left)
            # Link the previous node (tail) with the current node
            if tail:
                tail.right = node
                node.left = tail
            else:
                # If this is the first node, assign it to head
                head = node
            # Move the tail to the current node
            tail = node
            dfs(node.right)

        head,tail = None,None

        dfs(root)
        # Perform in-order traversal to link nodes
        head.left = tail
        tail.right = head

        return head

    # Not in-place conversion using an auxiliary list
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # NOT in place involves creating a new linked list.
        # In place solution.
        # Time Complexity : O(N)
        # Space Complexity : O(N)
        if (root == None):
            return None

        # Helper function for in-order traversal that fills the list with node values
        def Prefix(root, res):
            if not root:
                return
            Prefix(root.left, res)
            res.append(root.val)
            Prefix(root.right, res)

        dummy_head = Node(0)
        dummy_tail = Node(0)
        current = dummy_head
        dummy_head.right = dummy_tail
        dummy_tail.left = dummy_head

        linear_tree = []
        # Perform in-order traversal and store node values in linear_tree
        Prefix(root, linear_tree)

        # Create the doubly linked list from the stored values
        for num in linear_tree:
            temp = Node(num)
            temp.right = current.right
            current.right.left = temp
            current.right = temp
            temp.left = current
            current = current.right

        dummy_tail.left.right = dummy_head.right
        dummy_head.right.left = dummy_tail.left

        return dummy_head.right

X = Solution()
root = Node(3)
root.left = Node(2)
root.left.left = Node(1)
root.right = Node(4)
root.right.right = Node(5)

curr = ans = X.treeToDoublyList(root)

loop_print_counter = 0
while(curr):
    print(curr.val)
    curr= curr.right
    if(curr==ans):
        break
print()
curr = ans = X.treeToDoublyListInPlace(root)
loop_print_counter = 0
while(curr):
    print(curr.val)
    curr= curr.right
    if(curr==ans):
        break




