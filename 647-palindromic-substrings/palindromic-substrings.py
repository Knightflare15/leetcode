class Solution:
    def countSubstrings(self, s: str) -> int:
        res = {}
        def expand(l,r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                res[s[l:r+1]] = res.get(s[l:r+1],0) +1
                l-=1
                r+=1
            return
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        ans = 0
        for i in res.values():
            ans+=i 
        return ans