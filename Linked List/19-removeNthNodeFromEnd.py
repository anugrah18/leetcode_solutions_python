# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        while(self):
            print(self.val)
            self= self.next

class Solution(object):
    def removeNthFromEnd(self, head, n):

        counter = 0
        dummyHead = ListNode(0)
        dummyHead.next = head
        ptr1 = dummyHead
        ptr2 = head

        while (ptr2):
            if (counter < n):
                counter += 1
            else:
                ptr1 = ptr1.next
            ptr2 = ptr2.next

        ptr1.next = ptr1.next.next

        return dummyHead.next

LL = ListNode(1)
LL.next = ListNode(2)
LL.next.next = ListNode(3)
LL.next.next.next = ListNode(4)
LL.next.next.next.next = ListNode(5)

X = Solution()
answer =X.removeNthFromEnd(LL,2)
answer.printList()


# Time Complexity : O(N)
# Space Complexity : O(1)



