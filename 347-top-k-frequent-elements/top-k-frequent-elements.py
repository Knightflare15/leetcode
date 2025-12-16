import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            d[i] = d.get(i,0)+1
        arr = list(d.items())
        res = sorted(arr,key = lambda x: x[1])
        ans = []
        while k>0:
            temp = res.pop()
            ans.append(temp[0])
            k-=1
        return ans

        
     
        