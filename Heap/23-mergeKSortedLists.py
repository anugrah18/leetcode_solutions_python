import heapq

class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        q = []
        head = point = ListNode(0)
        for l in lists:
            if l:
                # inserted 'id of l' in heap as l.val may be not unique for comparasion
                heapq.heappush(q, (l.val, id(l), l))

        while len(q) != 0:
            val, _id, node = heapq.heappop(q)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(q, (node.val, id(node), node))

        return head.next


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

X = Solution()
head = X.mergeKLists([l1,l2,l3])

while(head):
    print(head.val)
    head = head.next