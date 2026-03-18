import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 0
        q = deque([[0,0]])
        moves = {(0,1),(1,0)}
        mat = [ [0]*(n+1) for _ in range(m+1)]
        if n>0:
            mat[0][1] = 1
        else:
            mat[1][0] = 1
        while q:

            pos = q.popleft()
            i = pos[0]
            j = pos[1]
            if mat[i+1][j+1]>0:
                continue
            mat[i+1][j+1] = mat[i][j+1] + mat[i+1][j]
            if i+1<m and (i+1,j):
                q.append([i+1,j])
            if j+1<n and (i,j+1):
                q.append([i,j+1])

        return mat[m][n]
            
