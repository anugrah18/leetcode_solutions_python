
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        res1 = first = ListNode(0)
        res2 = second = ListNode(0)

        while (head):
            if head.val < x:
                res1.next = ListNode(head.val)
                res1 = res1.next
            else:
                res2.next = ListNode(head.val)
                res2 = res2.next
            head = head.next

        res1.next = second.next
        return first.next

node = ListNode(1)
node.next = ListNode(4)
node.next.next = ListNode(3)
node.next.next.next = ListNode(2)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(2)

X = Solution()
resNode = X.partition(node,3)

curr = resNode

while curr:
    print(curr.val)
    curr = curr.next


# Time Complexity : O(N)
# Space Complexity : O(N)