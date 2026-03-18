class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        d = set(wordDict)
        dp[0] = True
        prevWord = [0]

        for i in range(len(s)):
            for j in wordDict:
                if s[i-len(j)+1:i+1] == j and dp[i-len(j)+1]==True:
                    dp[i+1] = True

        return dp[len(s)]