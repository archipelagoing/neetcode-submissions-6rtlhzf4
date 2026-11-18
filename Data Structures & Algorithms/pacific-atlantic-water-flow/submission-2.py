class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # lest start with the dimensions of hte grid
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if((r,c) in visit or
               r < 0 or c < 0 or r == ROWS or c == COLS or
               heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r + 1,c,visit, heights[r][c])
            dfs(r - 1,c,visit, heights[r][c])
            dfs(r,c + 1,visit, heights[r][c])
            dfs(r,c - 1,visit, heights[r][c])
            

        # run dfs on the first row: pacific ocean
        # water from the ocean can only go from equal or greater values
        for c in range(COLS):
            dfs(0,c, pac, heights[0][c])
            dfs(ROWS-1,c, atl, heights[ROWS -1][c])
        for r in range(ROWS):
            dfs(r, 0 , pac, heights[r][0])
            dfs(r, COLS -1, atl, heights[r][COLS - 1])
        # atp we will have marked every position that can reach pacific and atlantic

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl: 
                    res.append([r,c])
        return res

# is it beter to use dfs or bfs?
# instead of going through every single cell, why dont we start from the apacific ocean, find all the cells that border the pacific ocean, and see what other nodes can reach the pacific ocean? 

