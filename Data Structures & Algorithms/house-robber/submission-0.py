# sol4: dynamic programming
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0

        for num in nums:
            temp = max(num +rob1, rob2)
            rob1 = rob2
            rob2  = temp
        return rob2


""""
1. initialize rob1 and rob2 to 0
2. iterate thru each house
3. take the maximum of the initial value + rob1, and rob2
4. set rob1 to rob2
5. set rob2 to temp
6return rob2

"""        