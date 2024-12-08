class Solution(object):
    def findJudge(self, n, trust):
        # Initialize two arrays to track in-degree and out-degree of each person
        # indegree[i] represents the number of people who trust person i
        # outdegree[i] represents the number of people person i trusts
        indegree = [0] * (n + 1)  # Array of size n+1 (1-based indexing)
        outdegree = [0] * (n + 1)

        # Iterate through the trust pairs
        for t in trust:
            # For a trust pair [a, b], a trusts b
            indegree[t[1]] += 1  # Increment in-degree of b (person being trusted)
            outdegree[t[0]] += 1  # Increment out-degree of a (person trusting)

        # Iterate through all people (1 to n) to find the judge
        for i in range(1, n + 1):
            # A judge is trusted by everyone (in-degree == n-1) and trusts no one (out-degree == 0)
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i  # Return the judge's number

        # If no judge is found, return -1
        return -1

# Example usage:
X = Solution()

trust = [[1, 3], [2, 3]]  # Person 1 and 2 trust person 3
print(X.findJudge(3, trust))  # Output: 3 (person 3 is the judge)

# Time Complexity: O(E)
# - Where E is the number of edges in the trust list. Each edge is processed once to update in-degree and out-degree.

# Space Complexity: O(N)
# - Space is used for the in-degree and out-degree arrays of size n+1.
