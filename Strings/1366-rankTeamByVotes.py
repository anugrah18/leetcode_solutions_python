class Solution:
    def rankTeam(self, votes):
        x = len(votes[0])
        rank = {}

        for word in votes:
            for i,char in enumerate(word):
                if char not in rank:
                    rank[char] = [0]*x
                rank[char][i] = rank[char][i]+1

        rank = list(rank.items())
        rank.sort(reverse=True, key=lambda x: (x[1], [-ord(x[0])]))

        rank = [i[0] for i in rank]
        return ''.join(rank)


X = Solution()
print(X.rankTeam(["BCA","CAB","CBA","ABC","ACB","BAC"]))


# Time Complexity : O((M)log(M)) + O(NM) , M = number of votes , N = Number of teams
# Space Complexity : O(N^2) , N=number of teams