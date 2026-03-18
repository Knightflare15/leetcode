class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        coin = set(coins)
        for i in range(amount):
            if i+1 in coin:
                dp[i+1] = 1
                continue
            for itr in coins:
                if i+1-itr >=0 and dp[i+1-itr]!=0:
                   dp[i+1] = min(dp[i+1],dp[i-itr+1])
            if dp[i+1] != 0:
                dp[i+1]+=1

        return dp[amount] if dp[amount]!=float('inf') else -1 
