class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        x = {}
        y = {}
        def find(n):
            if parent[n]!=n:
                parent[n] = find(parent[n])
            return parent[n]
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa
        for i in range(len(stones)):
            parent[i] = i
        for i in range(len(stones)):
            xi, yi = stones[i]
            if xi in x:
                union(i, x[xi])
            else:
                x[xi] = i
            if yi in y:
                union(i, y[yi])
            else:
                y[yi] = i
        roots = set(find(i) for i in parent)
        return len(stones) - len(roots)
            
        


       



        