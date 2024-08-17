# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        # Initialize a ListNode with a value and a pointer to the next node
        self.val = val
        self.next = next

    def printList(self):
        # Method to print the values in the linked list
        while self:
            print(self.val)
            self = self.next


class Solution(object):
    # Method to find the middle node of a linked list
    def middleNode(self, head):
        # Initialize two pointers, slow and fast, both starting at the head of the list
        slow = fast = head

        # Traverse the list with fast moving twice as fast as slow
        while fast and fast.next:
            slow = slow.next  # slow pointer moves one step
            fast = fast.next.next  # fast pointer moves two steps

        # When fast reaches the end, slow will be at the middle
        return slow


# Create a linked list 1 -> 2 -> 3 -> 4 -> 5
LL = ListNode(1)
LL.next = ListNode(2)
LL.next.next = ListNode(3)
LL.next.next.next = ListNode(4)
LL.next.next.next.next = ListNode(5)

# Find the middle node of the linked list
X = Solution()
Partitioned_LL = X.middleNode(LL)

# Print the list starting from the middle node
Partitioned_LL.printList()

# Time Complexity : O(N) where N is the number of nodes in the linked list
# Space Complexity : O(1) as only two pointers are used