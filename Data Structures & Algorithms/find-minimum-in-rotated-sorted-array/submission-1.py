'''
In a rotated sorted array, the minimum element is the 
first element of the rotated portion.
Using binary search, we compare the middle value with the rightmost value:

If nums[mid] < nums[right], then the 
minimum lies in the left half (including mid).
Otherwise, the minimum lies in the right half (excluding mid).
This behaves exactly like finding a lower bound, gradually 
shrinking the search space until only the minimum remains.
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums) - 1

        while l < r:
            m = l + ( r-l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
            
            