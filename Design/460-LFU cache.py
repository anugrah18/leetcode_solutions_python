from collections import defaultdict,OrderedDict

class Node:
    def __init__(self, value, count):
        self.val = value
        self.count = count

# Time Complexity : O(1) for both operations put and get
# Space Complexity: O(N)

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeKeys = {}
        self.nodeCounts = defaultdict(OrderedDict)
        self.minCount = None

    def get(self, key: int) -> int:
        if key not in self.nodeKeys:
            return -1

        # Remove from the nodeCount bucket.
        node = self.nodeKeys[key]
        del self.nodeCounts[node.count][key]

        # Remove the zero count bucket.
        if not self.nodeCounts[node.count]:
            del self.nodeCounts[node.count]

        # Add the node in the bucket based on its frequency.
        node.count += 1
        self.nodeCounts[node.count][key] = node

        if not self.nodeCounts[self.minCount]:
            self.minCount += 1

        return node.val

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return

        # Replace value of node with key
        if key in self.nodeKeys:
            self.nodeKeys[key].val = value
            self.get(key)
            return

        if len(self.nodeKeys) == self.capacity:
            # Remove last item within minimum frequency bucket.
            lfuKey, lfuCount = self.nodeCounts[self.minCount].popitem(last=False)
            del self.nodeKeys[lfuKey]

        # Add the item
        newNode = Node(value, 1)
        self.nodeKeys[key] = newNode
        self.nodeCounts[1][key] = newNode
        self.minCount = 1

lfu= LFUCache(2)
print(lfu.put(1, 1))
print(lfu.put(2, 2))
print(lfu.get(1))
print(lfu.put(3, 3))
print(lfu.get(2))
print(lfu.get(3))
print(lfu.put(4, 4))
print(lfu.get(1))
print(lfu.get(3))
print(lfu.get(4))

