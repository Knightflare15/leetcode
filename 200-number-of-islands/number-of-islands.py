class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        moves = [(1,0),(0,1),(-1,0),(0,-1)]
        length = len(grid)
        height = len(grid[0])
        islands = 0
        def dfs(grid,i,j):
            if grid[i][j] == "0":
                return
            visited.add((i,j))
            for m in moves:
                dx  = i+m[0]
                dy = j+m[1]
                if dx >=0 and dx<length and dy >=0 and dy < height and (dx,dy) not in visited:
                    dfs(grid,dx,dy)
            return
    
        for i in range(length):
            for j in range(height):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(grid,i,j)
                    islands+=1
                        
        return islands