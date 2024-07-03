import heapq

class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        q = []  # Initialize a priority queue (min-heap)
        head = point = ListNode(0)  # Create a dummy head for the result list

        # Push the first node of each list into the heap
        for l in lists:
            if l:
                # Insert (value, id of node, node) into the heap
                # The id is used to avoid comparison issues when values are the same
                heapq.heappush(q, (l.val, id(l), l))

        # Extract the smallest element from the heap and add it to the result list
        while len(q) != 0:
            val, _id, node = heapq.heappop(q)  # Pop the smallest element
            point.next = ListNode(val)  # Add the smallest value to the result list
            point = point.next  # Move the pointer forward
            node = node.next  # Move to the next node in the list
            if node:  # If the list is not empty, push the next node into the heap
                heapq.heappush(q, (node.val, id(node), node))

        return head.next  # Return the merged list, skipping the dummy head


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

X = Solution()
head = X.mergeKLists([l1,l2,l3])

while(head):
    print(head.val)
    head = head.next


# Time Complexity : O(Nlogk) , where k is number of lists , N is the total number of nodes across all lists.
# Space Complexity : O(k)
