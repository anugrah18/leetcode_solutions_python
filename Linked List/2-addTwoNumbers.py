class ListNode(object):
    def __init__(self, val=0, next=None):
        # Initialize a ListNode with a value and a reference to the next node
        self.val = val
        self.next = next

    def printList(self):
        # Function to print the values in the linked list
        cur = self
        while cur is not None:
            print(cur.val)
            cur = cur.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Initialize a dummy node to hold the result list and a tail pointer
        ans = ListNode(0)
        ans_tail = ans
        carry = 0  # Initialize carry for sum overflow

        # Iterate through both linked lists until both are fully traversed
        while l1 or l2:
            # Get the values from the current nodes of both lists, default to 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the digit and the new carry
            out = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10

            # Create a new node with the sum result and move the tail pointer
            ans_tail.next = ListNode(out)
            ans_tail = ans_tail.next

            # Move to the next nodes in l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # If there is any carry left after the loop, add it as a new node
        if carry > 0:
            ans_tail.next = ListNode(carry)

        # Return the next of dummy node as the starting node of the result list
        return ans.next


# Create first linked list: 2 -> 4 -> 9
list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(9)

# Create second linked list: 5 -> 6 -> 4
list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)

# Add the two numbers represented by the linked lists
X = Solution()
res = X.addTwoNumbers(list1, list2)

# Print the result list
res.printList()  # Expected output: 7 -> 0 -> 4 -> 1

# Time Complexity : O(N)
# Where N is the length of the longer linked list. We iterate through each node once.

# Space Complexity : O(N)
# The space used is for the output linked list, which has at most max(length of l1, length of l2) + 1 nodes.
