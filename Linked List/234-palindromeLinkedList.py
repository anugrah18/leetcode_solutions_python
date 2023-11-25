# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):

        if (head == None or head.next == None):
            return True
        slow = head
        fast = head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

        slow = self.reverse(slow)
        fast = head

        while (slow != None):
            if (slow.val != fast.val):
                return False
            fast = fast.next
            slow = slow.next
        return True

    def reverse(self, node):
        prev = None
        while (node):
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode

        return prev

X =Solution()
ll = ListNode(1)
ll.next = ListNode(2)
ll.next = ListNode(1)
print(X.isPalindrome(ll))

# Time Complexity : O(N)
# Space Complexity : O(1)