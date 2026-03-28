class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp =[0]*(len(cost)+2)
        for i in range(3,len(cost)+2):
            dp[i] = min(dp[i-2]+cost[i-3],dp[i-1]+cost[i-2])

        return dp[len(cost)+1]