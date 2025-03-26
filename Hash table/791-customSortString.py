class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Step 1: Count frequency of each character in s
        dict = {}
        for ch in s:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1

        ans = []

        # Step 2: Add characters according to the order string
        for ch in order:
            if ch in dict:
                ans.append(ch * dict[ch])  # Repeat character by its count
                del dict[ch]  # Remove to avoid re-processing

        # Step 3: Add remaining characters not in order
        for ch, count in dict.items():
            ans.append(ch * count)

        return ''.join(ans)


X = Solution()
print(X.customSortString("bcafg", "abcd"))

# Time Complexity : O(N+M), N = length of s , M = length of order
# Space Complexity : O(N+M)
