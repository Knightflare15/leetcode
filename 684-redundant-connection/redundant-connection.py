class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [0]*(len(edges)+1)
        parent = [i for i in range(len(edges)+1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            px = find(x)
            py = find(y)

            if px == py:
                return True
            if rank[px]>rank[py]:
                parent[py] = px
            elif rank[py]>rank[px]:
                parent[px] = py
            else:
                parent[px] = py
                rank[py]+=1
            return False
        for i,j in edges:
            if union(i,j):
                return [i,j]
        return []


         
            
        