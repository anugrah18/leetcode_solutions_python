class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):

        if (head == None or head.next == None):
            return head

        mid = self._findMiddle(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self._merge(left, right)

    def _merge(self, list1, list2):
        dummyHead = ListNode()
        tail = dummyHead

        while (list1 and list2):
            if (list1.val <= list2.val):
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next

        tail.next = list1 if list1 != None else list2

        return dummyHead.next

    def _findMiddle(self, head):
        ptr1 = head
        ptr2 = head
        prev = None

        while (ptr2 and ptr2.next):
            prev = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        # To partition list and node before middle disconnected to middle
        if prev:
            prev.next = None

        return ptr1

node = ListNode(3)
node.next = ListNode(5)
node.next.next = ListNode(1)
node.next.next.next = ListNode(2)
node.next.next.next.next = ListNode(4)

X = Solution()
ans = X.sortList(node)

ptr = ans
while ptr:
    print(ptr.val)
    ptr = ptr.next

# Time Complexity = O(NLogN)
# Space Complexity = o(1)