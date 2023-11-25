from math import sqrt

# Efficient using sqrt
class Solution(object):
    def countPrimes_I(self, n: int) -> int:
        if n <= 2:
            return 0
        numbers = [False, False] + [True] * (n - 2)
        for p in range(2, int(sqrt(n)) + 1):
            if numbers[p]:

                for multiple in range(p * p, n, p):
                    numbers[multiple] = False


        return sum(numbers)

    def countPrimes_II(self, n):
        if (n < 3):
            return 0
        dict = {}
        count = 0

        for i in range(2, n):
            dict[i] = True

        dict[n] = False

        for i in range(2, n + 1):
            if (dict[i] == True):
                for j in range(2, int(n / i) + 1):
                    dict[i * j] = False;

        for i in dict:
            if (dict[i] == True):
                count = count + 1

        return count

X =Solution()
print(X.countPrimes_I(10))

# Time Complexity : O(sqrt(N)*p)
# Space Complexity : O(N)





