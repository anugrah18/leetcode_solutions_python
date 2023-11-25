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
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while (curr):
            if (val == curr.val):
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
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

# Time Complexity : O(N)
# Space Complexity : O(1)
