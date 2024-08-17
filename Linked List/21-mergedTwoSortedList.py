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
    def mergeTwoLists(self, l1, l2):
        # Create a prehead node to act as a starting point
        prehead = ListNode(-1)
        prev = prehead

        # Traverse both lists and merge them in sorted order
        while l1 and l2:
            if l1.val <= l2.val:
                # If l1's value is smaller or equal, link it to the merged list
                prev.next = l1
                l1 = l1.next
            else:
                # If l2's value is smaller, link it to the merged list
                prev.next = l2
                l2 = l2.next
            # Move the prev pointer to the last node in the merged list
            prev = prev.next

        # If either list is not fully traversed, link the remaining nodes
        prev.next = l1 if l1 else l2

        # Return the head of the merged list, which is the next node after prehead
        return prehead.next

# Create two sorted linked lists
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# Merge the two lists
X = Solution()
answer1 = X.mergeTwoLists(l1, l2)

# Print the merged list
answer1.printList()

# Time Complexity : O(N + M), where N and M are the lengths of the two linked lists l1 and l2
# Space Complexity : O(1), only a few pointers are used for merging