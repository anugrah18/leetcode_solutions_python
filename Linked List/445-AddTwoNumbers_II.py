# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        # Initialize a ListNode with a value and a reference to the next node
        self.val = val
        self.next = next

    def printList(self):
        # Function to print the values in the linked list
        while self:
            print(self.val)
            self = self.next


class Solution(object):
    # Approach 1 - Convert to stack
    # Time Complexity: O(N), where N is the maximum length of the two lists
    # Space Complexity: O(N), due to the use of stacks to store the values from the lists
    def addTwoNumbers_1(self, l1, l2):
        stack_1 = []
        stack_2 = []

        # Push all values from the first list into stack_1
        while l1:
            stack_1.append(l1.val)
            l1 = l1.next

        # Push all values from the second list into stack_2
        while l2:
            stack_2.append(l2.val)
            l2 = l2.next

        carry = 0
        newHead = None

        # Process the stacks until both are empty and no carry is left
        while stack_1 or stack_2 or carry != 0:
            # Pop values from stacks or use 0 if the stack is empty
            val1 = stack_1.pop() if stack_1 else 0
            val2 = stack_2.pop() if stack_2 else 0

            # Calculate the sum and update carry
            s = val1 + val2 + carry
            carry = s // 10

            # Create a new node with the digit result and link it to the new head
            node = ListNode(s % 10)
            node.next = newHead
            newHead = node

        return newHead


    # Approach 2 - Convert to numbers
    # Time Complexity: O(N), where N is the maximum length of the two lists
    # Space Complexity: O(N), due to the space needed to store the integer and the resulting linked list
    def addTwoNumbers_2(self, l1, l2):
        n1 = 0
        n2 = 0

        # Convert the first linked list to a number
        while l1:
            n1 = 10 * n1 + l1.val
            l1 = l1.next

        # Convert the second linked list to a number
        while l2:
            n2 = 10 * n2 + l2.val
            l2 = l2.next

        # Add the two numbers
        n = n1 + n2

        # Create a new linked list from the result
        root = curr = ListNode(0)
        for i in str(n):
            curr.next = ListNode(int(i))
            curr = curr.next

        return root.next


# Example usage:

# Create the first linked list: 7 -> 2 -> 4 -> 3
L1 = ListNode(7)
L1.next = ListNode(2)
L1.next.next = ListNode(4)
L1.next.next.next = ListNode(3)

# Create the second linked list: 5 -> 6 -> 4
L2 = ListNode(5)
L2.next = ListNode(6)
L2.next.next = ListNode(4)

X = Solution()

# Add the two numbers using the first approach (using stacks)
L3 = X.addTwoNumbers_1(L1, L2)
# Add the two numbers using the second approach (converting to numbers)
L4 = X.addTwoNumbers_2(L1, L2)

# Print the results
L3.printList()  # Expected output: 7 -> 8 -> 0 -> 7
L4.printList()  # Expected output: 7 -> 8 -> 0 -> 7
