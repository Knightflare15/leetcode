class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispal(stre,i,j):

            while i<j:
                if stre[i] != stre[j]:
                    return False
                i+=1
                j-=1
            return True

        def bt(s,i,arr):
            nonlocal res
            for itr in range(i-1,-1,-1):
                if ispal(s,itr,i-1):
                    arr.append(s[itr:i])
                    bt(s,itr,arr)
                    arr.pop()
            if i==0:
                res.append(arr[:])
        s = s[::-1]
        bt(s,len(s),[])
        return res