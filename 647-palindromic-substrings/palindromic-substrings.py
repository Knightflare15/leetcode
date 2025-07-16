class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count=0
        dp = [[False]*(n) for _ in range(n)]
     
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=True
                    count+=1
                    continue
                if s[i]==s[j] and (dp[i+1][j-1] if j-1>i else True) :
                    dp[i][j]=True
                    count+=1

                
        return count