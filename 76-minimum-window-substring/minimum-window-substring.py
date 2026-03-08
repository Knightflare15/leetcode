class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        ans = ""
        for i in t:
            d[i] = d.get(i,0)+1
        length = len(t)
        l = 0
        r = 0
        while r< len(s):
            while l<=r and s[l] not in d :
                l+=1
            if s[r] in d:
                d[s[r]]-=1
                if d[s[r]]>=0:
                    length-=1
            while length == 0:
                if (len(ans)>r-l+1 or len(ans)==0):
                    ans= s[l:r+1]
                if s[l] in d:
                    d[s[l]]+=1
                    if d[s[l]] > 0:
                        length += 1
                l+=1 
            r+=1

        return ans