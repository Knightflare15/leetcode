class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        arr = [float('inf')] * n
        arr[0] = 0
        visited = set()
        total = 0

        for _ in range(n):
            min_val = float('inf')
            u = -1
            for i in range(n):
                if i not in visited and arr[i] < min_val:
                    min_val = arr[i]
                    u = i

            visited.add(u)
            total += min_val

            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    arr[v] = min(arr[v], dist)

        return total