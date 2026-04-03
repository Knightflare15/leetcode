class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i,sumo):
            if i == len(nums) and sumo == target:
                return 1
            if i>=len(nums):
                return 0
            if (i,sumo) in memo:
                return memo[(i,sumo)]
            memo[(i,sumo)] = dfs(i+1,sumo-nums[i])+(dfs(i+1,sumo+nums[i]))
            return memo[(i,sumo)]
        return dfs(0,0) 