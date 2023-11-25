class HitCounter:

    def __init__(self):
        self.queue = []

    def hit(self, timestamp) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp):
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.pop(0)
        return len(self.queue)

X = HitCounter()
X.hit(1)
X.hit(7)
print(X.getHits(250))
X.hit(251)
X.hit(299)
X.hit(301)
print(X.getHits(302))

# Time Complexity : O(1) for hit and O(N) for getHits
# Space Complexity: O(N)