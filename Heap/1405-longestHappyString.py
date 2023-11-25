import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = []
        if a > 0:
            freq.append([-a, 'a'])
        if b > 0:
            freq.append([-b, 'b'])
        if c > 0:
            freq.append([-c, 'c'])

        heapq.heapify(freq)
        ans = ""
        while freq:
            cnt, char = heapq.heappop(freq)
            if len(ans) > 1 and ans[-1] == ans[-2] == char:
                if not freq:
                    break
                cnt2, char2 = heapq.heappop(freq)
                ans += char2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(freq, [cnt2, char2])
            else:
                ans += char
                cnt += 1
            if cnt:
                heapq.heappush(freq, [cnt, char])

        return ans


X = Solution()
print(X.longestDiverseString(1,1,7))


# Time Complexity : O(klogN) , k = number of characters
# Space Complexity : O(2*k)