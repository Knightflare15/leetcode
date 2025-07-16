class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPal(s):
            return s == s[::-1]

        dp = []
        dp = [0]*(len(s)+1)
        dp[1]=1
        for i in range(2,len(s)+1):
            dp[i]=dp[i-1]+1
            for j in range(i-1):
                if isPal(s[j:i]):
                    dp[i]+=1
        return dp[len(s)]