class Solution:
    #approach 1
    # Time Complexity : O(N)
    # Space Complexity : O(N)
    def compress_1(self, chars):
        ans = ""
        count = 0
        for c in chars:
            if len(ans) == 0:
                ans += c
                count = 1
            elif ans[-1] == c:
                count += 1
            else:
                if count != 1:
                    ans += str(count)
                ans += c
                count = 1

        if count != 1:
            ans += str(count)

        N = min(len(ans), len(chars))

        if N == len(ans):
            for i in range(0, N):
                chars[i] = ans[i]
        return N

    # approach 2
    # Time Complexity : O(N)
    # Space Complexity : O(1)
    def compress_2(self, chars):
        readIndex = writeIndex = 0

        while readIndex < len(chars):
            count = 0
            letter = chars[readIndex]
            while readIndex < len(chars) and chars[readIndex] == letter:
                readIndex += 1
                count += 1

            chars[writeIndex] = letter
            writeIndex += 1
            if count > 1:
                for s in str(count):
                    chars[writeIndex] = s
                    writeIndex += 1

        return writeIndex




X = Solution()
print(X.compress_1(["a","a","b","b","c","c","c"]))
print(X.compress_2(["a","a","b","b","c","c","c"]))






