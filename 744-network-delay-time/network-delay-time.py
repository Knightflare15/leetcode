class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mat = [[float('inf')]*n for i in range(n)]
        for i in times:
            mat[i[0]-1][i[1]-1] = i[2]
        length = 0
        visited = set()
        k = k-1
        arr = [float('inf')]*len(mat)
        arr[k] = 0
        while len(visited)<len(mat):
            visited.add(k)
            mini = float('inf')
            mini_idx = k
            for i in range(len(arr)):
                if i != k:
                    arr[i] = min(arr[i],mat[k][i]+arr[k])
                    if arr[i]<mini and i not in visited:
                        mini = arr[i]
                        mini_idx = i
            if mini_idx == k:
                break
            k = mini_idx    
        return max(arr) if len(visited)==len(mat) else -1
