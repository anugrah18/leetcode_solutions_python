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
    # Function to remove the nth node from the end of a linked list
    # Time Complexity: O(N), where N is the number of nodes in the linked list
    # Space Complexity: O(1)
    def removeNthFromEnd(self, head, n):
        # Initialize a counter to track the position
        counter = 0

        # Create a dummy node that points to the head of the list
        dummyHead = ListNode(0)
        dummyHead.next = head

        # Initialize two pointers: ptr1 (slow pointer) and ptr2 (fast pointer)
        ptr1 = dummyHead
        ptr2 = head

        # Move ptr2 ahead by n nodes
        while ptr2:
            if counter < n:
                counter += 1
            else:
                # Once counter reaches n, start moving ptr1 along with ptr2
                ptr1 = ptr1.next
            ptr2 = ptr2.next

        # Skip the nth node from the end by adjusting the next pointer of ptr1
        ptr1.next = ptr1.next.next

        # Return the new head of the list
        return dummyHead.next



LL = ListNode(1)
LL.next = ListNode(2)
LL.next.next = ListNode(3)
LL.next.next.next = ListNode(4)
LL.next.next.next.next = ListNode(5)

X = Solution()
answer =X.removeNthFromEnd(LL,2)
answer.printList()


# Time Complexity: O(N), where N is the number of nodes in the linked list.
# Space Complexity: O(1), since no extra space is used apart from a few pointers.


