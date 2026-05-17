class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        temp = {}
        for i in s:
            d[i] = d.get(i,0)+1
        i = 0
        start = i
        res = []
        while i < len(s):
            temp[s[i]] = temp.get(s[i],0)+1
            if all(temp[t] == d[t] for t in temp):
                res.append(i-start+1)
                i+=1
                start = i
                temp = {}
                continue
            i+=1
        return res if res else [len(s)]


