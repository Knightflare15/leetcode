class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        res = [0] * (l + 1)
        res[l] = 1 
        for i in range(l - 1, -1, -1):
            if s[i] == "0":
                res[i] = 0
            else:
                res[i] = res[i + 1]
                if i + 1 < l and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                    res[i] += res[i + 2]
                    
        return res[0]