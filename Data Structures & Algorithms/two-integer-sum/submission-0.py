class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make 2 loops, j should iterate through everything past i
        for i in range(len(nums)):
            for j in range( i+1, len(nums)):
                if nums[i]+ nums[j]==target:
                    return [i,j]