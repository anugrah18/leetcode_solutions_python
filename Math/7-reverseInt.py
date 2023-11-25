class Solution(object):
    def reverse(self, x):

        sign = 1 if x > 0 else -1
        max = (2 ** 31) - 1 if x > 0 else 2 ** 31
        x = abs(x)
        q = x
        r = 0
        rev = 0
        while (q > 0):
            q, r = divmod(q, 10)
            # To check rev does not overflow int limit
            if (rev > int(max / 10)):
                return 0
            rev = rev * 10 + r

        return rev * sign


X =Solution()
print(X.reverse(-125))