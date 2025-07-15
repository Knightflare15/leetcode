class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        moves = ((1,0),(0,1),(-1,0),(0,-1))
        m = len(mat)
        n = len(mat[0])
        p = deque()
        cpy = [[-1 for i in mat[0]] for j in mat] 
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    cpy[i][j]=0
                    p.append((i,j))
        count =0
        while p:
            s = len(p)
            for l in range(s):
                node = p.popleft()
                if cpy[node[0]][node[1]]==-2:
                    cpy[node[0]][node[1]]=count
                for i in moves:
                    tmp = (node[0]+i[0],node[1]+i[1])
                    if tmp[0]>=0 and tmp[1]>=0 and tmp[0]<m and tmp[1]<n and cpy[tmp[0]][tmp[1]]==-1:
                        cpy[tmp[0]][tmp[1]]=-2
                        p.append(tmp)
            count+=1

        return cpy
            
            

                
