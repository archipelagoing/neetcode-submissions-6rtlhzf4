class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        #BACKTRACKING   
        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or # not the same character board & word
                (r,c) in path): # visiting the same position twice
                return False

            path.add((r,c))
            res =  (dfs(r+1, c, i+1) or
                    dfs(r-1, c, i+1) or 
                    dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1))

            path.remove((r,c))
            return res 

            # but we havent actually run this dfs for teh whole board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):return True
        return False

        # time complexity is gonna be o(n *m*dfs [4^n])
        # remember we're calling dfs 4 times 4^len(word)


"""
wordle  
"""