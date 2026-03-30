class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1. Sorting.
        #Time: O(nlogn + mlogm)
        #Space: o(1) or o(n+m)
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        # true if equal, false if not.

# 1. Sorting:
# a) F: if lengths of both strings are different
# b) sort both strings & compare
# c) T: if sorted are equal
# d) F: else

