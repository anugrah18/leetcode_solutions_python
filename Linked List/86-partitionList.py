
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        # Create two dummy nodes to start the two partitions
        res1 = first = ListNode(0)  # This will hold nodes less than x
        res2 = second = ListNode(0)  # This will hold nodes greater than or equal to x

        # Traverse the original linked list
        while head:
            # If the current node's value is less than x, add it to the first partition
            if head.val < x:
                res1.next = ListNode(head.val)
                res1 = res1.next
            # If the current node's value is greater than or equal to x, add it to the second partition
            else:
                res2.next = ListNode(head.val)
                res2 = res2.next
            # Move to the next node in the original list
            head = head.next

        # Connect the end of the first partition to the beginning of the second partition
        res1.next = second.next
        # Return the start of the first partition, which is the new head of the modified list
        return first.next

node = ListNode(1)
node.next = ListNode(4)
node.next.next = ListNode(3)
node.next.next.next = ListNode(2)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(2)

X = Solution()
resNode = X.partition(node,3)

curr = resNode

while curr:
    print(curr.val)
    curr = curr.next


# Time Complexity : O(N)
# Space Complexity : O(N)