class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        moves = [[-1,0],[1,0],[0,1],[0,-1]]
        visitededge = set()
        m = len(board)
        n = len(board[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j >= n :
                return False
            if board[i][j] == "X" or (i,j) in visited:
                return True
            visited.add((i,j))
            res = True
            for x,y in moves:
                ni = x+i
                nj = y+j
                res = res and dfs(ni,nj)
            return res
        visited = set()
        for i in range(m):
            for j in range(n):
                found = False
                if board[i][j] == "O":
                    found = dfs(i,j)
                if found:
                    for itrX,itrY in visited:
                        board[itrX][itrY] = "X"
                visited.clear()
                
        return