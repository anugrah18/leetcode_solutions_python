import heapq

class Solution:
# Using Greedy approach.
# Time Complexity : O(N) , N = number of tasks
# Space Complexity : O(1)
    def leastInterval_I(self, tasks, n):

        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1

        freq.sort()

        # max_frequency
        f_max = freq.pop()
        idle_time = (f_max - 1) * n

        while freq:
            idle_time -= min(f_max - 1, freq.pop())

        idle_time = max(0, idle_time)

        return idle_time + len(tasks)

# Using maxHeap.
# Time Complexity : O(N) , N = number of tasks
# Space Complexity : O(N)
    def leastInterval_II(self, tasks, n):
        dict = {}
        maxHeap = []
        for t in tasks:
            dict[t] = dict.get(t, 0) - 1

        for k in dict:
            maxHeap.append(dict[k])

        heapq.heapify(maxHeap)

        time = 0
        q = []

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.pop(0)[0])

        return time


X =Solution()
print(X.leastInterval_I(["A","A","A","A","A","A","B","C","D","E","F","G"],2))
print(X.leastInterval_II(["A","A","A","A","A","A","B","C","D","E","F","G"],2))