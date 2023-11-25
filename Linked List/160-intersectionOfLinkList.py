class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode_I(self, headA, headB):
        # Time Complexity : O(N+M) , N = nodes in list A, M = node in list B
        # Space Complexity : O(M)

        head1 = headA
        head2 = headB
        dict = {}
        while (head1 != None):
            if (head1 not in dict):
                dict[head1] = "occupied"
            head1 = head1.next

        while (head2 != None):
            if (head2 in dict):
                return head2
            head2 = head2.next

        return None

    def getIntersectionNode_II(self, headA: ListNode, headB: ListNode):
        # Time Complexity : O(N+M) , N = nodes in list A, M = node in list B
        # Space Complexity : O(1)

        ptr1 = headA
        ptr2 = headB

        if ptr1 == None or ptr2 == None:
            return None

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

            if ptr1 == ptr2:
                return ptr1

            if ptr1 == None:
                ptr1 = headB

            if ptr2 == None:
                ptr2 = headA

        return ptr1

LL1 = ListNode(4)
LL1.next = ListNode(7)
LL1.next.next = ListNode(8)
LL1.next.next.next = ListNode(3)

LL2 = ListNode(1)
LL2.next = ListNode(6)
LL2.next.next = LL1.next

X = Solution()
print(X.getIntersectionNode_I(LL1,LL2).val)
print(X.getIntersectionNode_II(LL1,LL2).val)


