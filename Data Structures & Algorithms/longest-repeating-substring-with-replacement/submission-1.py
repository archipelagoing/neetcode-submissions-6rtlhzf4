class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        val = 0
        for i in range(len(s)):
            count, maxf = {}, 0  # frequency map
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max( maxf, count[s[j]])
# If the window size minus maxf is <= k, it is valid.
                if(j-i +1) - maxf <= k:
# Update res with the window size.
                    val = max(val, j-i + 1)
# Return res after testing all starting positions.
        return val
        