class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Algorithm
        # 1. If t is empty, return "".
        if t == "":
            return ""

        # 2. Build a frequency map countT for characters in t.
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # 3. Initialize:
        #     a. window as an empty map for the current window counts.
        #     b. have = 0 = how many characters currently meet the required count.
        #     c. need = len(countT) = how many distinct characters we need to match.
        #     d. res = [-1, -1] and resLen = infinity to store the best window.
        window = {}
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        # 4. Use a right pointer r to expand the window over s:
        for r in range(len(s)):
            #     4.a. Add s[r] to window.
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            #     4.b. If s[r] is in countT and its count in window matches countT, increment have.
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # 5.a. Update the best result if the current window is smaller.
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # 5.b.i. Decrease the count of s[l] in window.
                window[s[l]] -= 1
                
                # 5.b.ii. If s[l] is in countT and its count in window falls below countT, decrement have.
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                # 5.b.iii. Move l right.
                l += 1
        
        # 6. After the loop, return the substring defined by res if found; otherwise, return "".
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
            

# Algorithm
# 1. If t is empty, return "".
# 2. Build a frequency map countT for characters in t.
# 3. Initialize:
#     a. window as an empty map for the current window counts.
#     b. have = 0 = how many characters currently meet the required count.
#     c. need = len(countT) = how many distinct characters we need to match.
#     d. res = [-1, -1] and resLen = infinity to store the best window.
# 4. Use a right pointer r to expand the window over s:
#     a. Add s[r] to window.
#     b. If s[r] is in countT and its count in window matches countT, increment have.


# 5. When have == need, the window is valid:
#     a. Update the best result if the current window is smaller.
#     b. Then shrink from the left:
#         i. Decrease the count of s[l] in window.
#         ii. If s[l] is in countT and its count in window falls below countT, decrement have.
#         iii. Move l right.
# 6. After the loop, return the substring defined by res if found; otherwise, return "".

# Intuition
# We want the smallest window in s that contains all characters of t (with the right counts).
# Instead of checking all substrings, we use a sliding window:
#       . Expand the window by moving the right pointer r and adding characters into a window map.
#       . Once the window has all required characters (i.e., it "covers" t), we try to shrink it from the left with pointer l to make it as small as possible while still valid.
# During this process, we keep track of the best (smallest) window seen so far.
# This way, we only scan each character at most two times, making it efficient and still easy to follow.
