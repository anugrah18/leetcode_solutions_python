class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self,head):
        curr = head

        while(curr and curr.next):
            if(curr.val == curr.next.val):
                curr.next = curr.next.next
            else:
                curr = curr.next

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


