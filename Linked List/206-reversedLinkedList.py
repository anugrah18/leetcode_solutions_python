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

        pastNode = None
        currentNode = head

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = pastNode
            pastNode = currentNode
            currentNode = nextNode
        head = pastNode
        return head

list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)

X = Solution()
rev = X.reverseList(list)

rev.printList()

# Time Complexity : O(N)
# Space Complexity : O(1)