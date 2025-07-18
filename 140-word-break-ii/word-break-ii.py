class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n=len(s)
        finalRes= []

        result = []
        tmp = ""
        def wb(i,res):
            if i==n and res=="":
                finalRes.append(" ".join(result))
                return 
            if i==n:
                return 
            res+=s[i]
            if res in wordDict:
                wb(i+1,res)
                result.append(res)
                wb(i+1,"")
                result.pop()
            else:
                wb(i+1,res) 
        res = []
        flag = wb(0,"")
        return finalRes