# Floyd's Marshall Algorithm
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float('inf')] * n  # Initialize cost to reach each city as infinity
        prices[src] = 0  # Cost to reach the source city is 0

        # Perform k+1 rounds of edge relaxation (to allow up to k stops)
        for i in range(k + 1):
            tmpPrices = prices.copy()  # Make a copy to avoid overwriting prices in the same round
            for s, d, p in flights:  # For each flight (source, destination, price)
                if prices[s] == float('inf'):
                    continue  # Skip if source city is not yet reachable
                # Relax the edge if a cheaper price is found via this route
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices  # Update prices for the next round

        # If destination is unreachable, return -1
        return -1 if prices[dst] == float('inf') else prices[dst]


X = Solution()
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
print(X.findCheapestPrice(4, flights, 0, 3, 1))

# Time Complexity :  O(KE) , where  e = number of flights (edges)
# Space Complexity : O(N)
