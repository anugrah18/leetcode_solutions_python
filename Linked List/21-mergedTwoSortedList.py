# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        while (self):
            print(self.val)
            self = self.next

class Solution(object):
    # Time Complexity : O(N)
    # Space Complexity : O(1)
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2=l2.next
            prev = prev.next

        prev.next = l1 if l1 else l2
        return prehead.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

X = Solution()
answer1 = X.mergeTwoLists(l1, l2)
answer1.printList()
