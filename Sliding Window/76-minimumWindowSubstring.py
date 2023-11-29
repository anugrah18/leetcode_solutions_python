class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Check if t is an empty string
        if t == "":
            return ""

        # Dictionary to store the count of characters in string t
        countT, window = {}, {}

        # Populate countT with the count of characters in string t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Variables to track the number of characters needed and currently have
        have, need = 0, len(countT)

        # Variables to store the result indices and length
        res, resLen = [-1, -1], float('inf')

        # Left pointer for the sliding window
        l = 0

        # Iterate through the string using the right pointer 'r'
        for r in range(len(s)):
            c = s[r]

            # Update the count of the current character in the window
            window[c] = 1 + window.get(c, 0)

            # Check if the count of the current character reaches the required count in t
            if c in countT and window[c] == countT[c]:
                have += 1

            # Check if all characters in t are found in the current window
            while have == need:
                # Update the result if the current window is smaller than the previous result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Update the window
                window[s[l]] -= 1

                # Update the 'have' count if the character at 'l' is in t and the count is less than required
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # Move the left pointer 'l' forward
                l += 1

        # Extract the result substring based on the indices
        l, r = res
        return s[l:r + 1] if resLen != float('inf') else ""


X = Solution()
print(X.minWindow("ADOBECODEBANC","ABC"))

# Time Complexity : O(n) where n = len(s)
# Space complexity : O(m) m = len(t)