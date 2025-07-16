class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        res = [-1]
        tmp = ""
        for i in range(m):
            tmp+=s[i]
            if tmp in wordDict:
                res.append(i)
                tmp = ""
                continue
            for j in res:
                if s[j+1:i+1] in wordDict:
                    res.append(i)
                    tmp = ""
                    break
        if tmp == "":
            return True
        return False