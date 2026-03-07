class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        idx = defaultdict(list)
        dic = set()
        for i in strs:
            temp = "".join(sorted(i))
            if temp in dic:
                idx[temp].append(i)
            else:
                idx[temp]=[i]
                dic.add(temp)
        res = []
        for i in idx:
            res.append(idx[i])
        return res
        