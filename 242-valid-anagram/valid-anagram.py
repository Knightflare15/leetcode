class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapp = dict()
        for i in s:
            mapp[i] = mapp.get(i,0)+1
        for i in t:
            mapp[i] = mapp.get(i,0)-1
            if mapp[i]==0:
                mapp.pop(i,None)
        if not mapp:
            return True
        return False
            