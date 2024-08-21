# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

     def printList(self):
         cur = self
         while (cur != None):
             print(cur.val)
             cur = cur.next


class Solution(object):
    def reverseList(self, head):
        prev = None  # Initialize the previous pointer as None
        curr = head  # Start with the current pointer at the head of the list

        # Iterate through the list
        while curr:
            nxt = curr.next  # Temporarily store the next node
            curr.next = prev  # Reverse the current node's pointer to the previous node
            prev = curr  # Move the previous pointer to the current node
            curr = nxt  # Move the current pointer to the next node

        return prev  # Return the new head of the reversed list, which is the last non-null node

list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)

X = Solution()
rev = X.reverseList(list)

rev.printList()

# Time Complexity : O(N)
# Space Complexity : O(1)