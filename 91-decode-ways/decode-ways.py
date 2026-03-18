class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        res = [0]*(l+1)
        res[0] = 1
        for i in range(l):
            if i>0 and s[i]!="0" and 10<int(s[i-1:i+1])<=26 :
                res[i+1] = res[i] + res[i-1]
                continue
                
            elif i>0 and s[i] == "0" and s[i-1:i+1] in {"10","20"}:
                res[i+1] = res[i-1]
                continue
            elif s[i] == "0":
                return 0
            else:
                res[i+1] = res[i]


        print(res)          
        return res[l]