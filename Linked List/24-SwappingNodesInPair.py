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
    def swapPairs(self, head):

        dummy = ListNode(-1)
        dummy.next = head
        prev_node= dummy

        while(head and head.next):
            first_node = head
            second_node = head.next

            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = first_node
            head = first_node.next

        return dummy.next

LL = ListNode(1)
LL.next = ListNode(2)
LL.next.next = ListNode(3)
LL.next.next.next = ListNode(4)
X = Solution()
new_LL = X.swapPairs(LL)
new_LL.printList()

# Time Complexity : O(N)
# Space Complexity : O(1)


