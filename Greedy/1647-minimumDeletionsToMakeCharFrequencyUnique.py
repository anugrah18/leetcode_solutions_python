class Solution:
    def minDeletion_I(self,s):
        # Time Complexity : O(N)
        # Space Complexity : O(N)
        # Store the frequency of each character
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord('a')] += 1

        delete_count = 0
        # Use a set to store the frequencies we have already seen
        seen_frequencies = set()
        for i in range(26):
            # Keep decrementing the frequency until it is unique
            while frequency[i] and frequency[i] in seen_frequencies:
                frequency[i] -= 1
                delete_count += 1

            # Add the newly occupied frequency to the set
            seen_frequencies.add(frequency[i])

        return delete_count

    def minDeletion_II(self,s):
        # Time Complexity : O(N)
        # Space Complexity : O(N)
        freq=[0]*26
        count=0

        for c in s:
            freq[ord(c)-ord('a')]+=1

        freq = sorted(freq,reverse=True)

        freq_limit = freq[0]-1

        for i in range(1,len(freq)):
            if freq[i]<=freq_limit:
                freq_limit = freq[i]-1
            else:
                count+= freq[i]-freq_limit
                freq_limit-=1

            freq_limit=max(freq_limit,0)

        return count



X = Solution()
print(X.minDeletion_I('aaabbbccc'))
print(X.minDeletion_II('aaabbbccc'))