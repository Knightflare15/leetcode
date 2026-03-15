class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in prerequisites:
            graph[i[1]].append(i[0])
        visited = set()
        visiting = set()
        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)
            for j in graph[i]:
                flag = dfs(j)
                if not flag:
                    return False
            visiting.remove(i)
            visited.add(i)
            return True
        for i in range(numCourses):
            flag = dfs(i)
            if not flag:
                return flag 
        return True

