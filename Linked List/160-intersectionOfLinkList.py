class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        # Initialize two pointers, one for each list
        ptr1 = headA
        ptr2 = headB

        # If either list is empty, there can be no intersection
        if ptr1 is None or ptr2 is None:
            return None

        # Traverse both lists
        while ptr1 != ptr2:
            # Move both pointers one step at a time
            ptr1 = ptr1.next
            ptr2 = ptr2.next

            # If they meet at the same node, that node is the intersection
            if ptr1 == ptr2:
                return ptr1

            # If ptr1 reaches the end of list A, switch to the beginning of list B
            if ptr1 is None:
                ptr1 = headB

            # If ptr2 reaches the end of list B, switch to the beginning of list A
            if ptr2 is None:
                ptr2 = headA

        # Either both pointers meet at the intersection, or both become None (no intersection)
        return ptr1

LL1 = ListNode(4)
LL1.next = ListNode(7)
LL1.next.next = ListNode(8)
LL1.next.next.next = ListNode(3)

LL2 = ListNode(1)
LL2.next = ListNode(6)
LL2.next.next = LL1.next

X = Solution()
print(X.getIntersectionNode(LL1,LL2).val)

# Time Complexity : O(N+M) , N = nodes in list A, M = node in list B
# Space Complexity : O(1)
