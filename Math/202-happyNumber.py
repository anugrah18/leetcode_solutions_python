def getNext(n):
    totalSum = 0
    while n > 0:
        n, digit = divmod(n, 10)
        totalSum = totalSum + digit ** 2
    return totalSum


class Solution(object):
    def isHappy(self, n):
        ht = set()
        while (n != 1):
            ht.add(n)
            n = getNext(n)
            if (n in ht):
                return False

        return True

X = Solution()
print(X.isHappy(19))





