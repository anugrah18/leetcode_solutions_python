class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        curr = head

        # Traverse the linked list
        while curr and curr.next:
            # If the current node's value is the same as the next node's value
            if curr.val == curr.next.val:
                # Skip the next node by pointing the current node's next to the node after the next
                curr.next = curr.next.next
            else:
                # Move to the next node
                curr = curr.next

        # Return the modified list with duplicates removed
        return head


X= Solution()
head= ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head = X.deleteDuplicates(head)

while(head):
    print(head.val)
    head=head.next

# Time Complexity = O(N)
# Space Complexity = O(1)


