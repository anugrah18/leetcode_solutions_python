class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        # Base case: if the list is empty or contains only one element, it's already sorted
        if head is None or head.next is None:
            return head

        # Find the middle of the list
        mid = self._findMiddle(head)

        # Recursively sort the left and right halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the sorted halves
        return self._merge(left, right)

    def _merge(self, list1, list2):
        # Create a dummy head to help with merging the lists
        dummyHead = ListNode()
        tail = dummyHead

        # Merge the two sorted lists
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Append any remaining elements from either list
        tail.next = list1 if list1 is not None else list2

        # Return the merged list, skipping the dummy head
        return dummyHead.next

    def _findMiddle(self, head):
        # Use the slow and fast pointer approach to find the middle of the list
        ptr1 = head
        ptr2 = head
        prev = None

        while ptr2 and ptr2.next:
            prev = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next

        # Disconnect the first half of the list from the middle to partition it
        if prev:
            prev.next = None

        # Return the start of the second half of the list
        return ptr1


node = ListNode(3)
node.next = ListNode(5)
node.next.next = ListNode(1)
node.next.next.next = ListNode(2)
node.next.next.next.next = ListNode(4)

X = Solution()
ans = X.sortList(node)

ptr = ans
while ptr:
    print(ptr.val)
    ptr = ptr.next

# Time Complexity = O(NLogN)
# Space Complexity = o(1)