class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^res
        return res

# # if 2 bits are the same XOR 
#  0 ^ 0 = 1
#  1 ^ 0 = 1
