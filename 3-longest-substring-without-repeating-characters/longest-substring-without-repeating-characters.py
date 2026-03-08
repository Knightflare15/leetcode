class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        rep = {}
        length = 0

        while r<len(s):
            rep[s[r]] = rep.get(s[r],0)+1
            while rep[s[r]] > 1:
                rep[s[l]]-=1
                l+=1
            length = max(length,r-l+1)
            r+=1
        return length