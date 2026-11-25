# MATH 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # how tf do we find the missing numer here
        # why is it called bit manipulation
        # WHY DO I NEED TO FIND AN EVEN FASTER RUNTIME
        res = len(nums)
        for i in range(len(nums)):
            print("i", i, "nums[i]", nums[i])
            print("resb4", res)
            res += i - nums[i]
            print("res", res)

        return res

