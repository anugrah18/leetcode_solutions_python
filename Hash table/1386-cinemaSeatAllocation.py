class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        ans = 0
        seats = {}
        for r, c in reservedSeats:
            if r not in seats:
                seats[r] = []
            seats[r].append(c)

        for r in seats:
            two = {2, 3, 4, 5}
            four = {4, 5, 6, 7}
            six = {6, 7, 8, 9}
            for c in seats[r]:
                if c in two:
                    two.remove(c)
                if c in four:
                    four.remove(c)
                if c in six:
                    six.remove(c)
            ans += max(len(four) == 4, (len(two) == 4) + (len(six) == 4))

        ans += 2 * (n - len(seats))
        return ans

X = Solution()
print(X.maxNumberOfFamilies(3,[[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))

# Time Complexity : O(N) , N = number of reserved Seats
# Space Complexity : O(RC) , R = number of rows , C = number of cols
