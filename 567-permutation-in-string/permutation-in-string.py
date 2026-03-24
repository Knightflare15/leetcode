class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d={}
        match =0
        for i in s1:
            match+=1
            d[i] = d.get(i,0)+1
        length = len(s1)
        l=0
        r = 0
        while r<len(s2):
            if s2[r] in d:
                d[s2[r]]-=1
            if r-l>=length:
                    if s2[l] in d:
                        d[s2[l]]+=1
                    l+=1
            if all(v == 0 for v in d.values()):
                print(d)
                return True    
            r+=1
                
        print(d)
        return False
        