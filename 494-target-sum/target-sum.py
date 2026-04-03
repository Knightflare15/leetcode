class Solution:
    def findTargetSumWays(self, nums, target):
        total = sum(nums)

        # edge case
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0

        s = (target + total) // 2

        dp = [0] * (s + 1)
        dp[0] = 1

        for num in nums:
            for i in range(s, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[s]