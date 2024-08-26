class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        # Dictionary to map old nodes to their corresponding new (copied) nodes.
        # Initialize with {None: None} to handle cases where a node's next or random pointer is None.
        oldToCopy = {None: None}

        # First pass: Create all the new nodes and store them in the dictionary.
        curr = head
        while curr:
            copy = Node(curr.val)  # Create a new node with the same value as the current node.
            oldToCopy[curr] = copy  # Map the original node to its copy.
            curr = curr.next  # Move to the next node in the original list.

        # Second pass: Assign next and random pointers for the copied nodes.
        curr = head
        while curr:
            copy = oldToCopy[curr]  # Get the copied node from the dictionary.
            copy.next = oldToCopy[curr.next]  # Assign the next pointer in the copied list.
            copy.random = oldToCopy[curr.random]  # Assign the random pointer in the copied list.
            curr = curr.next  # Move to the next node in the original list.

        # Return the head of the copied list.
        return oldToCopy[head]


# Example Usage:
# Creating the original list:
# Node 1 -> Node 2 -> Node 3
# Random pointers:
# Node 1 -> Node 3, Node 2 -> Node 1, Node 3 -> Node 2

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

node1.random = node3
node2.random = node1
node3.random = node2

# Solution instance
X = Solution()

# Create a deep copy of the list
copied_list_head = X.copyRandomList(node1)

# Traverse the copied list to show it is correctly copied
curr = copied_list_head
while curr:
    random_val = curr.random.val if curr.random else None
    print(f"Node Value: {curr.val}, Random points to: {random_val}")
    curr = curr.next

# Time Complexity = O(N)
# Space Complexity = O(N)