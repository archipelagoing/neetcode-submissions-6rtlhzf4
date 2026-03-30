# 1. initilize 2 pointers
#     a. l at start of string
#     b r at end of string
# 2. While l is less than r:
#     a. move l forward until it points to an alphanumeric char
#     b. move r backwards until it points to an alphanumeric character
#     c. Compare lowercase characters at l and r
#         i. If they dont match, return false
#     d. Move both pointers inward: l+=1, r -=1
# 3. If the loop finishes without mimatches, return true
# time o(n) space 0(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # now they both pointing at an alphanumeric caracter
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True

    def alphaNum (self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
