from collections import OrderedDict


class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

# Using Ordered Dictionary
# Time Complexity : O(1) for both operations put and get
# Space Complexity: O(capactiy)
class LRUCache_I:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ordList = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.ordList:
            return -1
        self.ordList.move_to_end(key)
        return self.ordList[key]

    def put(self, key: int, value: int) -> None:
        if key in self.ordList:
            self.ordList.move_to_end(key)
        self.ordList[key] = value

        if len(self.ordList) > self.capacity:
            self.ordList.popitem(last=False)


# Using Double Linked List
# Time Complexity : O(1) for both operations put and get
# Space Complexity: O(capactiy)
class LRUCache_II():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)

        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)

LRU = LRUCache_I(3)
print(LRU.put(1,1))
print(LRU.put(2,2))
print(LRU.put(3,3))
print(LRU.get(1))
print(LRU.put(4,4))
print(LRU.get(2))

LRU = LRUCache_II(3)
print(LRU.put(1,1))
print(LRU.put(2,2))
print(LRU.put(3,3))
print(LRU.get(1))
print(LRU.put(4,4))
print(LRU.get(2))
