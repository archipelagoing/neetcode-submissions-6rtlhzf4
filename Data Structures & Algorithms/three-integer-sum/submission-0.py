class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            
            l,r = i+1, len(nums) - 1
            while l < r :
                threeSum = a + nums[l] +nums[r]
                if threeSum > 0:
                    r -= 1 # <-
                elif threeSum < 0: 
                    l += 1 # ->
                else: 
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
        
# 1.  Sort the array to handle duplicates and enable two-pointer logic.
# 2. Loop through the array using index i:
#   i. Let a = nums[i].
#   ii. If a > 0, break (all remaining numbers are positive).
# iii. Skip duplicate values for the first number.
# 3. Set two pointers:
#    i. l = i + 1
#   ii. r = len(nums) - 1
# 4. While l < r:
#    i. Compute threeSum = a + nums[l] + nums[r].
#   ii. If threeSum > 0, move r left.
#   iii. If threeSum < 0, move l right.
#   iv. If threeSum == 0:
#        a. Add the triplet to the result.
#        b. Move both pointers inward.
#        c. Skip duplicates at the left pointer.
# 5. Return the list of all valid triplets.