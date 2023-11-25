class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.queue = []

    def next(self, val):
        size, queue = self.size, self.queue
        if (len(queue) < self.size):
            queue.append(val)
        else:
            queue.pop(0)
            queue.append(val)

        window_sum = sum(queue[-size:])
        return (window_sum / min(len(queue), size))


X = MovingAverage(3)
print(X.next(1))
print(X.next(10))
print(X.next(3))
print(X.next(5))

# Time Complexity : O(1)
# Space Complexity : O(N)