class Solution:
    def fullJustify(self, words, maxWidth):
        lst = []
        res = []
        n = 0
        for w in words:

            while len(w) + n + len(lst) > maxWidth:
                # Calculate gaps between words in list.
                gaps = (len(lst) - 1) or 1

                # Calculate spaces need based on gaps.
                q, rem = divmod(maxWidth - n, gaps)

                # Adding spaces for each word in list.
                for i in range(gaps):
                    lst[i] += " " * q + (" " if i < rem else "")

                # Append line with spaces to result.
                res.append("".join(lst))
                # Reset characters length and list.
                n, lst = 0, []

            # Append words in list.
            lst.append(w)
            # Calculating number of characters.
            n += len(w)
        # Left justify the result.
        return res + [" ".join(lst).ljust(maxWidth)] if lst else []



X = Solution()
print(X.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))





