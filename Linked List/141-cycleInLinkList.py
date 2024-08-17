class ListNode(object):
    def __init__(self, x):
        # Initialize a ListNode with a value and a reference to the next node
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        # If the list is empty or has only one node, it cannot have a cycle
        if not head or not head.next:
            return False

        # Initialize two pointers, slow and fast
        slow = fast = head

        # Traverse the list with both pointers
        while fast and fast.next:
            slow = slow.next           # Move slow pointer one step
            fast = fast.next.next      # Move fast pointer two steps

            # If slow pointer and fast pointer meet, there is a cycle
            if slow == fast:
                return True

        # If the loop exits, no cycle was detected
        return False

# Example usage:
X = Solution()

# Create a linked list: 1 -> 2 -> 3 -> 4 -> (cycle back to 2)
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
list.next.next.next.next = list.next  # Creates a cycle

print(X.hasCycle(list))  # Expected output: True

# Time Complexity: O(N), where N is the number of nodes in the linked list.
# Space Complexity: O(1), only a constant amount of extra space is used.
