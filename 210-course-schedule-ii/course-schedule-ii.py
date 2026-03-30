class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(set)
        inv = {}
        res = []
        for i in range(numCourses):
            d[i] = set()
            inv[i] = 0
        for i,j in prerequisites:
            d[i].add(j)
            inv[i]+=1
        arr = deque()
        for i in d:
            if inv[i] == 0:
                arr.append(i)
        while arr:
            node = arr.popleft()
            res.append(node)
            for i,j in prerequisites:
                if node in d[i]:
                    d[i].remove(node)
                    inv[i]-=1
                    if inv[i] == 0:
                        arr.append(i) 

        return res if len(res)==len(inv) else []

            
            
        