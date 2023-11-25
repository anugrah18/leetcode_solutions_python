class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res

X = Codec()
Z = Codec()
Y = X.encode(["Hello","World"])
Z = Z.decode(Y)
print(Y)
print(Z)

# Time Complexity : O(N)
# Space Complexity : O(N)


