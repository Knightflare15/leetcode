class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = []
        dp = [0]*(len(s)+1)
        dp[1]=1
        for i in range(2,len(s)+1):
            dp[i]=dp[i-1]+1
            for j in range(i-1):
                if  s[j:i] == s[j:i][::-1]:
                    dp[i]+=1
        return dp[len(s)]