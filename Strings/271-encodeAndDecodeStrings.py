class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""  # Result string to store the encoded version
        for s in strs:
            # For each string, store its length followed by a '#' and then the string itself
            res += str(len(s)) + "#" + s
        return res  # Return the encoded string

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        res, i = [], 0  # Initialize result list and index

        while i < len(s):
            j = i
            # Find the position of the next '#'
            while s[j] != "#":
                j += 1
            # Get the length of the next string
            length = int(s[i:j])
            # Extract the string of that length after the '#'
            res.append(s[j + 1: j + 1 + length])
            # Move index to the start of the next length information
            i = j + 1 + length
        return res  # Return the list of decoded strings

X = Codec()
Z = Codec()
Y = X.encode(["Hello","World"])
Z = Z.decode(Y)
print(Y)
print(Z)

# Time Complexity : O(N)
# Space Complexity : O(1)


