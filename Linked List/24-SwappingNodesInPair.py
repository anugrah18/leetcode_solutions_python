# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        while(self):
            print(self.val)
            self = self.next

class Solution(object):
    def swapPairs(self, head):
        # Create a dummy node to serve as the previous node for the head.
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy

        # Traverse the list in pairs
        while head and head.next:
            # Identify the nodes to be swapped
            first_node = head
            second_node = head.next

            # Perform the swap by adjusting the pointers
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Move the prev_node and head pointers forward to the next pair
            prev_node = first_node
            head = first_node.next

        # Return the new head of the list (next node after dummy)
        return dummy.next


LL = ListNode(1)
LL.next = ListNode(2)
LL.next.next = ListNode(3)
LL.next.next.next = ListNode(4)
X = Solution()
new_LL = X.swapPairs(LL)
new_LL.printList()

# Time Complexity : O(N)
# Space Complexity : O(1)


