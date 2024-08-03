class Solution:
    def rankTeam(self, votes):
        # Get the length of a single vote string (number of teams)
        x = len(votes[0])
        # Dictionary to store the rank counts for each team
        rank = {}

        # Iterate over each vote
        for word in votes:
            # Iterate over each character in the vote (each team)
            for i, char in enumerate(word):
                # If the team is not yet in the rank dictionary, add it with a list of zeros
                if char not in rank:
                    rank[char] = [0] * x
                # Increment the count of the team's rank at position i
                rank[char][i] += 1

        # Convert the rank dictionary to a list of tuples for sorting
        rank = list(rank.items())
        # Sort the teams first by their rank counts in descending order, then by team letter in ascending order
        rank.sort(reverse=True, key=lambda x: (x[1], [-ord(x[0])]))

        # Extract the sorted team letters
        rank = [i[0] for i in rank]
        # Join the sorted team letters into a single string and return it
        return ''.join(rank)

# Example usage
X = Solution()
print(X.rankTeam(["ABC","ACB","ABC","ACB","ACB"]))

# Time Complexity: O(M * log(M)) + O(N * M), where M is the number of votes and N is the number of teams
# Space Complexity: O(N^2), where N is the number of teams
