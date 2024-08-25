class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # Helper function to reverse `k` nodes in the linked list.
        def reverseLinkedList(head, k):
            new_head = None
            ptr = head

            # Reverse `k` nodes in the linked list.
            while k:
                next_node = ptr.next
                ptr.next = new_head
                new_head = ptr
                ptr = next_node
                k -= 1

            return new_head

        ptr = head  # Pointer to traverse the list
        ktail = None  # Tail of the last reversed k-group
        new_head = None  # New head of the modified list

        # Iterate through the list to process groups of size `k`.
        while ptr:
            count = 0
            ptr = head

            # Check if there are at least `k` nodes left to reverse.
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            if count == k:
                # Reverse the current group of `k` nodes.
                revHead = reverseLinkedList(head, k)

                # Set the new head if it's the first group.
                if not new_head:
                    new_head = revHead

                # Connect the last group's tail to the current group's head.
                if ktail:
                    ktail.next = revHead

                # Update the tail to the current group's original head.
                ktail = head
                # Move the head pointer to the next group.
                head = ptr

        # If there are nodes left that are fewer than `k`, attach them as is.
        if ktail:
            ktail.next = head

        # Return the new head of the modified list.
        return new_head if new_head else head



# Example usage:
linklist = ListNode(1)
linklist.next = ListNode(2)
linklist.next.next = ListNode(3)
linklist.next.next.next = ListNode(4)
linklist.next.next.next.next = ListNode(5)

X = Solution()
ans = X.reverseKGroup(linklist, 2)

# Print the reversed list in groups of 2.
while ans:
    print(ans.val)
    ans = ans.next

# Time Complexity: O(N)
# The entire list is traversed, and each node is processed exactly once, leading to O(N) time complexity.
# Space Complexity: O(1)
# The algorithm uses a constant amount of extra space, apart from the input and output structures.
