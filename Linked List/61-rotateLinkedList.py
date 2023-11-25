class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if (head == None):
            return head

        ptr = head
        N = 1

        while (ptr.next):
            N = N + 1
            ptr = ptr.next

        ptr.next = head
        tail_index = N - int(k % N) - 1

        ptr = head
        for i in range(0, tail_index):
            ptr = ptr.next

        newHead = ptr.next
        ptr.next = None

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




