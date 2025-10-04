class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}
        res = None
        def find(n):
            if parent[n]!=n:
                parent[n] = find(parent[n])
            return parent[n]
        def union(a,b):
            p1,p2 = find(a),find(b)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p2] > rank[p1]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1]+=1
            return True
        for i in range(len(edges)):
            parent[i+1]=i+1
            rank[i+1] = 0
        for e1,e2 in edges:
            if not union(e1,e2):
                return [e1,e2]
         
            
        