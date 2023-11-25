class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self,head,k):

        def reverseLinkedList(head,k):
            new_head = None
            ptr = head

            while k:
                next_node = ptr.next
                ptr.next = new_head
                new_head = ptr
                ptr = next_node
                k-=1

            return new_head

        ptr = head
        ktail = None
        new_head = None

        while ptr:
            count = 0
            ptr = head

            while count<k and ptr:
                ptr = ptr.next
                count+=1

            if count == k:
                revHead = reverseLinkedList(head,k)

                if not new_head:
                    new_head = revHead

                if ktail:
                    ktail.next = revHead

                ktail = head
                head = ptr

        if ktail:
            ktail.next = head

        return new_head if new_head else head


linklist = ListNode(1)
linklist.next = ListNode(2)
linklist.next.next = ListNode(3)
linklist.next.next.next = ListNode(4)
linklist.next.next.next.next = ListNode(5)

X = Solution()
ans = X.reverseKGroup(linklist,2)

while(ans):
    print(ans.val)
    ans = ans.next