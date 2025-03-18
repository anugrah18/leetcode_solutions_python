class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = []
        self.window_sum = 0

    def next(self, val: int) -> float:
        if len(self.queue)==self.size:
            self.window_sum -= self.queue.pop(0)
        self.window_sum+=val
        self.queue.append(val)

        return self.window_sum/min(self.size,len(self.queue))


X = MovingAverage(3)
print(X.next(1))
print(X.next(10))
print(X.next(3))
print(X.next(5))

# Time Complexity : O(1)
# Space Complexity : O(N) , N = size of the window