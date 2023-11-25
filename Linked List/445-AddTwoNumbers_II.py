# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        while(self):
            print(self.val)
            self=self.next


class Solution(object):
    # Approach 1 - Convert to numbers.
    def addTwoNumbers_1(self, l1, l2):

        n1 = 0
        n2 = 0

        while (l1):
            n1 = 10 * n1 + l1.val
            l1 = l1.next

        while (l2):
            n2 = 10 * n2 + l2.val
            l2 = l2.next

        n = n1 + n2
        root = curr = ListNode(0)

        for i in str(n):
            curr.next = ListNode(int(str(i)))
            curr = curr.next

        return root.next

    # Approach 2 - Convert to stack.
    # Time Complexity : O(N) , N = max length of two lists
    # Space Complexity : O(N) , N = max length of two lists
    def addTwoNumbers_2(self,l1,l2):
        stack_1 = []
        stack_2 = []

        while l1:
            stack_1.append(l1.val)
            l1 = l1.next

        while l2:
            stack_2.append(l2.val)
            l2 = l2.next

        carry = 0
        newHead = None

        while stack_1 or stack_2 or carry != 0:
            val1 = stack_1.pop() if stack_1 else 0
            val2 = stack_2.pop() if stack_2 else 0

            s = val1 + val2 + carry

            node = ListNode(s % 10)
            carry = s // 10

            node.next = newHead
            newHead = node

        return newHead

L1 = ListNode(7)
L1.next = ListNode(2)
L1.next.next = ListNode(4)
L1.next.next.next = ListNode(3)

L2 = ListNode(5)
L2.next = ListNode(6)
L2.next.next = ListNode(4)

X =Solution()
L3 = X.addTwoNumbers_1(L1,L2)
L4 = X.addTwoNumbers_2(L1,L2)

L3.printList()
L4.printList()