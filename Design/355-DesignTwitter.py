import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.count = 0  # Global timestamp counter (used to order tweets by recency)
        self.tweetMap = defaultdict(list)  # Maps userId -> list of [timestamp, tweetId]
        self.followMap = defaultdict(set)  # Maps userId -> set of followeeIds

    # Time complexity : O(1)
    # Space Complexity : O(1) per call
    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append the tweet with a timestamp (using negative count for max-heap behavior)
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1  # Decrement timestamp so newer tweets have smaller count (more recent)

    # Time complexity : O(NlogN)
    # Space Complexity : O(N) per call
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []  # Final result: list of tweetIds
        minHeap = []  # Min-heap (simulates max-heap using negative timestamps)

        # Ensure the user follows themselves to see their own tweets
        self.followMap[userId].add(userId)

        # Load the most recent tweet of each followee into the heap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1  # Most recent tweet index
                count, tweetId = self.tweetMap[followeeId][index]
                # Store: [timestamp, tweetId, followeeId, next_index_to_check]
                minHeap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(minHeap)

        # Extract the 10 most recent tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)  # Add the tweet to the result

            # If more tweets exist from this followee, push the next most recent
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    # Time complexity : O(1)
    # Space Complexity : O(1) per call
    def follow(self, followerId: int, followeeId: int) -> None:
        # Add followee to the follower's follow list
        self.followMap[followerId].add(followeeId)

    # Time complexity : O(1)
    # Space Complexity : O(1) per call
    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove followee if it exists in the follower's follow list
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Simulate usage
twitter = Twitter()  # "Twitter"         -> null
twitter.postTweet(1, 5)  # "postTweet"       -> null
print(twitter.getNewsFeed(1))  # "getNewsFeed"     -> [5]
twitter.follow(1, 2)  # "follow"          -> null
twitter.postTweet(2, 6)  # "postTweet"       -> null
print(twitter.getNewsFeed(1))  # "getNewsFeed"     -> [6, 5]
twitter.unfollow(1, 2)  # "unfollow"        -> null
print(twitter.getNewsFeed(1))  # "getNewsFeed"     -> [5]
