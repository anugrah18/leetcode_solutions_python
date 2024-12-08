class Solution(object):
    def findItinerary(self, tickets):
        # Create a graph to represent the flight connections
        graph = {}  # Dictionary where keys are departure airports and values are lists of destination airports
        ans = []  # List to store the final itinerary in reverse order

        # Build the graph from the tickets
        for ticket in tickets:
            # If the departure airport is not already in the graph, initialize it
            if ticket[0] not in graph:
                graph[ticket[0]] = []
            # Append to the existing list of destinations
            graph[ticket[0]].append(ticket[1])

        # Ensure lexical (alphabetical) order of destinations for each departure airport
        for node in graph:
            graph[node] = sorted(graph[node])  # Sort the list of destinations alphabetically

        # Depth-first search (DFS) to build the itinerary
        def dfs(src):
            # Check if the source airport has destinations
            if src in graph:
                # While there are destinations left for this airport
                while graph[src]:
                    # Pop the first (smallest lexicographical) destination and continue the DFS
                    dfs(graph[src].pop(0))
            # Append the current airport to the answer in reverse order
            ans.append(src)

        # Start the DFS from 'JFK' as it is always the starting point
        dfs('JFK')
        # Reverse the itinerary to get the correct order and return it
        return ans[::-1]

# Example usage:
X = Solution()
print(X.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
# Output: ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']

# Time Complexity: O(N log N)
# - Sorting the destinations for each airport takes O(N log N), where N is the number of tickets.
# - DFS traverses each ticket once, which takes O(N).

# Space Complexity: O(N)
# - The graph and answer list use space proportional to the number of tickets.
