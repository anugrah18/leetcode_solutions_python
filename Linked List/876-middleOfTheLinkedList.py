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
    def middleNode(self, head):

        slow = fast = head
        while (fast and fast.next):
            slow= slow.next
            fast = fast.next.next
        return slow


LL = ListNode(1)
LL.next = ListNode(2)
LL.next.next = ListNode(3)
LL.next.next.next = ListNode(4)
LL.next.next.next.next = ListNode(5)

X =Solution()
Partitioned_LL = X.middleNode(LL)
Partitioned_LL.printList()

# Time Complexity : O(N)
# Space Complexity : O(1)