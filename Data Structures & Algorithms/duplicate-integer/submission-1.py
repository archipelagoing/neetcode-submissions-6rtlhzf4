class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
# #   1. Brute force: check every pair of elements; 
# #   a) T: pair equal values
# #   b) F: else 
# #   Time: o(n^2) [2 arrays] 
# #   Space: o(1) [in place]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]== nums[j]:
#                     return True
#         return False

# # *****************************************
# # 2.  Sorting: sort array first; 
# #   a) T: check adjacent positions to detect duplicates; 
# #   b) F: else
# #   Time: O(nlogn) (timsort has this time compelxity)  
# #   Space: O(n) In-place sort for timsort
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 return True
#         return False


# # *****************************************
# # 3. Hash Set
# #     a) initialize empty hash set
# #     b) iterate thru each number in array
# #     c) T: if it is already in set, duplicate has been found
# #          else, add to set
# #     d) F: If loop finishes without finding any duplicate
# #     Time: O(n)
# #     Space:O(n)
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False 
        
# *****************************************
# 4. Hash Set Length
#     a) Convert array into hash set, removing duplicates
#     b) COmpare size of set with original array size
#     c) T: if set is smaller; duplicates must have been removed from the set
#     d) F: else
#     Time: O(n)
#     Space:O(n)
        return len(set(nums)) < len(nums)



