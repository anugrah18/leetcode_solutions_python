class Node(object):
    def __init__(self, val, prev, next, child):
        # Initialize a Node with a value, previous node, next node, and a child node
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        # If the head is None, return None (no nodes to flatten)
        if not head:
            return None

        # Create a pseudo head node to act as a starting point
        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead

        # Initialize a stack to help with flattening the list
        stack = []
        stack.append(head)

        while stack:
            # Pop the last node from the stack
            curr = stack.pop()

            # Link the previous node with the current node
            prev.next = curr
            curr.prev = prev

            # If the current node has a next node, push it onto the stack
            if curr.next:
                stack.append(curr.next)

            # If the current node has a child node, push it onto the stack
            if curr.child:
                stack.append(curr.child)
                # After processing the child, remove the child pointer
                curr.child = None

            # Move the prev pointer to the current node
            prev = curr

        # Detach the pseudo head from the real head
        pseudoHead.next.prev = None
        return pseudoHead.next

# Example Input:
# 1<->2<->4
#     |
#     3<->5<->6
#         |
#         7

# Create nodes
node1 = Node(1, None, None, None)
node2 = Node(2, None, None, None)
node3 = Node(3, None, None, None)
node4 = Node(4, None, None, None)
node5 = Node(5, None, None, None)
node6 = Node(6, None, None, None)
node7 = Node(7, None, None, None)

# Set up the doubly linked list structure with child pointers
node1.next = node2
node2.prev = node1
node2.next = node4
node4.prev = node2
node2.child = node3
node3.next = node5
node5.prev = node3
node5.child = node7
node5.next = node6
node6.prev = node5

# Flatten the list
X = Solution()
res = X.flatten(node1)

# Print the flattened list
while res:
    print(res.val)
    res = res.next

# Time Complexity: O(N), where N is the number of nodes in the linked list.
# Space Complexity: O(N), in the worst case, the stack will contain all nodes in the list.
