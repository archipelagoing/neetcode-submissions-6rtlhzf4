class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l]) # remove the left pointer
                l +=1
            charSet.add(s[r])
            res = max(res,r - l + 1) # update the result if current window size is greater than it is right now
        return res

        