class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        coin = set(coins)
        for i in range(amount):
            k = i+1
            if k in coin:
                dp[k] = 1
                continue
            for itr in coins:
                if k-itr >=0:
                   dp[k] = min(dp[k],dp[k-itr])
            if dp[k] != 0:
                dp[k]+=1

        return dp[amount] if dp[amount]!=float('inf') else -1 
