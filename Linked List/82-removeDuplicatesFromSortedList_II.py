class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy

        # Traverse the linked list.
        while curr:
            # If the current node's next two nodes exist and have the same value, skip the duplicates.
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                temp = curr.next.next
                # Move the temp pointer forward as long as it points to a node with the same value.
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                # Link the current node to the node after the duplicates.
                curr.next = temp.next
            else:
                # Move the current pointer forward if no duplicates are found.
                curr = curr.next

        # Return the modified list, starting after the dummy node.
        return dummy.next


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(4)
node.next.next.next.next.next = ListNode(4)
node.next.next.next.next.next.next = ListNode(5)

X = Solution()
ans = X.deleteDuplicates(node)

# Printing the resulting linked list.
curr = ans
while curr:
    print(curr.val)
    curr = curr.next

#Time Complexity: O(N)
#Space Complexity: O(1)