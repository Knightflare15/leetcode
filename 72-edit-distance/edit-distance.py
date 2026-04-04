class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ops = 0
        memo = {}
        def dfs(s1,s2):
            res = 0
            if s2>=len(word2):
                return len(word1) - s1
            if s1 >= len(word1):
                return len(word2) - s2
            if (s1,s2) in memo:
                return memo[(s1,s2)]
            if word1[s1] == word2[s2]:
                res = dfs(s1+1,s2+1)
            else:
                insert = 1+dfs(s1,s2+1)
                replace = 1+dfs(s1+1,s2+1)
                delete = 1+dfs(s1+1,s2)
                res = min(insert,delete,replace)
            memo[(s1,s2)] = res
            return memo[(s1,s2)]
            
        return dfs(0,0)
