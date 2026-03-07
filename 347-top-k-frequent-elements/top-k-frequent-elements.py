class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] = dic.get(i,0)+1
        res = []
        l = 0 
        sorted_dic = sorted(dic.items(), key=lambda x: x[1],reverse = True)
        rest = sorted_dic[:k]
        for i in rest:
            res.append(i[0])
        return res