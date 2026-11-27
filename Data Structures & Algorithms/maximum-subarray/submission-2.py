class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # at each step, decide to keep extending ( addc x) or reset ( start a new slice)
        # how? start a fresh slicer at x: 

        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)