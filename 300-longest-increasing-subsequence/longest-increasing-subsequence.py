import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        sumo = 0
        for num in nums:
            idx = bisect.bisect_left(dp,num)
            if len(dp) == idx:
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp) 
