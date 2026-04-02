class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        m = len(grid)
        n = len(grid[0])
        arr = grid
        q = []
        heapq.heappush(q,[grid[0][0],0,0])
        maxi = 0
        visited = set()
        while(q):
            val,i,j = heapq.heappop(q)
            maxi = max(val,maxi)
            visited.add((i,j))
            if i==m-1 and j==n-1:
                return maxi
            for x,y in moves:
                dx = i + x
                dy = j + y
                if 0<=dx<m and 0<=dy<n and (dx,dy) not in visited:
                    heapq.heappush(q,[grid[dx][dy],dx,dy])
            
        return -1