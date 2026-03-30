from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i+1) + dfs(i+2) # one step or 2 stps
        
        return dfs(0)
