class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        tempProfit = 0
        for x in prices:
            if x < lowest:
                lowest = x
            else:
                if x-lowest > tempProfit:
                    tempProfit = x-lowest
                    
        return tempProfit

"""
1. loop thru the List
2. make a variable that says the smallest price so far. 
3. make a temporary profit that says the largest profit
4. if the new variable at that iteration is greater than the 
"""
        