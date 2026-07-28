class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        print(ROWS)
        print(COLS)
        islands = 0

        def dfs(r,c):
            if (r <0 or c < 0 or 
                r>= ROWS or c >=COLS or
                grid[r][c] == "0"):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] =="1":
                    dfs(r,c)
                    islands += 1

        return islands

        """
        hello the chariot
        cound & return the number of islands.  
        how do i even go about this
        ok so if it was me i would want to get a count for the rows and columsn
        """