class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums)+1)
        dp[0] = 0
        sumo = 0
        for i in range(1,len(nums)+1):
            for j in range(i-1):
                if nums[j]<nums[i-1]:
                    dp[i]=max(dp[j+1]+1,dp[i])
            sumo = max(sumo,dp[i])
        return sumo 
