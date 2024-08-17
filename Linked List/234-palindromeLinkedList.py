# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        # Initialize a ListNode with a value and a pointer to the next node
        self.val = val
        self.next = next

class Solution(object):
    # Function to check if a linked list is a palindrome
    # Time Complexity: O(N) where N is the number of nodes in the linked list
    # Space Complexity: O(1) as the space used is constant
    def isPalindrome(self, head):
        # If the list is empty or has only one element, it's a palindrome
        if head == None or head.next == None:
            return True

        # Initialize two pointers, slow and fast
        slow = head
        fast = head

        # Move slow by 1 step and fast by 2 steps to find the middle of the list
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        slow = self.reverse(slow)
        fast = head

        # Compare the first half with the reversed second half
        while slow != None:
            if slow.val != fast.val:
                return False  # If mismatch found, it's not a palindrome
            fast = fast.next
            slow = slow.next

        return True  # If no mismatch found, it's a palindrome

    # Helper function to reverse a linked list
    def reverse(self, node):
        prev = None
        while node:
            nextNode = node.next  # Store the next node
            node.next = prev      # Reverse the current node's pointer
            prev = node           # Move prev to the current node
            node = nextNode       # Move to the next node

        return prev  # Return the new head of the reversed list

# Example usage:
X = Solution()
ll = ListNode(1)
ll.next = ListNode(2)
ll.next = ListNode(1)

# Check if the linked list is a palindrome
print(X.isPalindrome(ll))  # Output: True

# Time Complexity: O(N) where N is the length of the linked list.
# Space Complexity: O(1) as the space used is constant (only pointers are used).
