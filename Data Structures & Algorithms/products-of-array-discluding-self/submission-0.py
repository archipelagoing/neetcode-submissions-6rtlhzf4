class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeroes = 1,0
        for num in nums:
            if num:
                prod *= num
            else:
                zeroes += 1
        if zeroes > 1: return [0] * len(nums)
        
        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zeroes: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res