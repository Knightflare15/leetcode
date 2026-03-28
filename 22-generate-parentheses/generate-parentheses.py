import math
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bt(bal,s):
            nonlocal res
            if len(s)==(2*n) and bal==0:
                res.append(s)
                return
            if len(s)>=(2*n):
                return
            if bal>n or bal<0:
                return
            
            bt(bal+1,s+"(")
            bt(bal-1,s+")")
            return

        bt(0,"")
        return res