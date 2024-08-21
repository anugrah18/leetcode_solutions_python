# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        while(self):
            print(self.val)
            self = self.next

class Solution(object):
    # Function to remove all elements from a linked list that have a specific value
    # Time Complexity: O(N), where N is the number of nodes in the linked list
    # Space Complexity: O(1)
    def removeElements(self, head, val):
        # Create a dummy node to handle edge cases such as removing the head node
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers: prev points to the last node that is not removed,
        # curr is used to traverse the list
        prev = dummy
        curr = head

        # Traverse the linked list
        while curr:
            # If the current node's value is equal to the target value, skip it
            if curr.val == val:
                prev.next = curr.next
            else:
                # Otherwise, move the prev pointer to the current node
                prev = curr
            # Move to the next node
            curr = curr.next

        # Return the new head of the list, which is dummy.next
        return dummy.next




X =Solution()
LL = ListNode(1)
LL.next = ListNode(2)
LL.next.next = ListNode(6)
LL.next.next.next = ListNode(3)
LL.next.next.next.next = ListNode(4)
LL.next.next.next.next.next = ListNode(5)
LL.next.next.next.next.next.next = ListNode(6)

new_LL = X.removeElements(LL,6)
new_LL.printList()

# Time Complexity: O(N), where N is the number of nodes in the linked list. The list is traversed once.
# Space Complexity: O(1), since no extra space is used apart from a few pointers.
