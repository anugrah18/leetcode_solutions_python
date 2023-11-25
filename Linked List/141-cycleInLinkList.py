
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if (head == None or head.next == None):
            return False

        fast = head.next
        slow = head
        while (slow != fast):
            if (fast == None or fast.next == None):
                return False
            else:
                slow = slow.next
                fast = fast.next.next
        return True

X=Solution()

list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
list.next.next.next.next = list.next

print(X.hasCycle(list))

# Time Complexity : O(N)
# Space Complexity : O(1)
