class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        memo = {}
        def dfs(str1,str2,i):
            if  i == len(s3) and str1 == len(s1) and str2 == len(s2):
                return True
            if (str1,str2,i) in memo:
                return memo[(str1,str2,i)]
            res = False
            if str1<len(s1) and s1[str1] == s3[i]:
                res = res or dfs(str1+1,str2,i+1)
            if str2<len(s2) and s2[str2] == s3[i]:
                res = res or dfs(str1,str2+1,i+1)
            
            memo[(str1,str2,i)] = res or False
            return memo[(str1,str2,i)]
        return dfs(0,0,0)