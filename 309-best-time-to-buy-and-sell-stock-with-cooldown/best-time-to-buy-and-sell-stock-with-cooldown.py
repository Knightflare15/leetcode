class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i,state):
            if i >= len(prices):
                return 0
            if (i,state) in memo:
                return memo[(i,state)]
            if state>=0:
                a1 = prices[i]-state + dfs(i+2,-1)
                a2 = dfs(i+1,state)
            else:
                a1 = dfs(i+1,state)
                a2 = dfs(i+1,prices[i])
            memo[(i,state)] = max(a1,a2)
            return memo[(i,state)]
        return dfs(0,-1)