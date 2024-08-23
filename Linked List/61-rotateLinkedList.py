class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        # If the list is empty, return the head (None)
        if head is None:
            return head

        # Initialize a pointer to traverse the list and a variable to store the length of the list
        ptr = head
        N = 1

        # Traverse the list to find its length (N) and make the list circular by connecting the last node to the head
        while ptr.next:
            N += 1
            ptr = ptr.next

        # Connect the last node to the head, making the list circular
        ptr.next = head

        # Calculate the new tail index after rotating k times
        tail_index = N - int(k % N) - 1

        # Reset the pointer to the head and move it to the new tail position
        ptr = head
        for i in range(tail_index):
            ptr = ptr.next

        # The new head will be the next node after the new tail
        newHead = ptr.next

        # Break the circular link to finalize the rotated list
        ptr.next = None

        # Return the new head of the rotated list
        return newHead


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = None

X = Solution()
rotatedNode = X.rotateRight(node,2)
print(rotatedNode.val)

# Time Complexity : O(N)
# Space Complexity : O(1)




