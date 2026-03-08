class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        dic = {}
        maxi = 0
        while r<len(s):
            dic[s[r]] = dic.get(s[r],0)+1
            maxi = max(maxi,dic[s[r]])
            if r-l>=maxi + k:
                dic[s[l]]-=1
                l+=1
            r+=1
        return min(maxi+k,len(s))