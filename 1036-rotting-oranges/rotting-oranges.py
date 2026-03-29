from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        moves = ((1,0),(0,1),(0,-1),(-1,0))
        q = deque()
        m, n = len(grid), len(grid[0])
        fresh = set()
        maxi = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))

        h = len(q)

        while q:
            x, y = q.popleft()
            h -= 1
            
            for dx, dy in moves:
                ni, nj = x + dx, y + dy
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) in fresh:
                    grid[ni][nj] = 2
                    q.append((ni, nj))
                    fresh.remove((ni, nj))
            if h == 0:
                h = len(q)
                if h > 0:
                    maxi += 1
        return -1 if fresh else maxi