class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,maxP = 0,1,0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r # update l to be the right pointer return
            r += 1
        return maxP

"""
2 pointers Solution
- we want to buy at the low price (l), and sell at high price (r)
- r > l --> we can make a profit, so we update maximum
- r < l --> r is new l, cheaper buying price is always better
l = 0;  r=1; maxP = 0 track max profit
1. While r in the array
    if prices[r] > prices[l] --> compute profit & update maxP
    ow, move l to r ( cheaper buy price)
    r++
2. Return maxP
"""
        