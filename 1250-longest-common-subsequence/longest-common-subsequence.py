class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        momo = {}
        def dp(i,j):
            if i == -1 or j==-1:
                return 0
            if (i,j) in momo:
                return momo[(i,j)]
            
            
            if text1[i]==text2[j]:
                c = 1+ dp(i-1,j-1)
            else:
                c = max(dp(i-1,j),dp(i,j-1))
            momo[(i,j)]=c
            return c
        return dp(n-1,m-1)
        
        
