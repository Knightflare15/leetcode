class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)-1)
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        if len(nums)-1>1:
            dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        n = len(nums) - 1
        dp2 = [0]*(len(nums)-1)
        dp2[0] = nums[1]
        if len(nums) > 2:
            dp2[1] = max(nums[2],nums[1])
        for i in range(3,len(nums)):
            dp2[i-1] = max(dp2[i-2],dp2[i-3]+nums[i])
        print(dp)
        print(dp2)
        return max(dp[n-1],dp2[n-1])