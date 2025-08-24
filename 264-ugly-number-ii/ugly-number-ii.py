import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        res = []
        heapq.heappush(heap,1)
        s = set()
        while len(res)<=n:
                itr = heapq.heappop(heap)
                if itr in s:
                    continue
                heapq.heappush(heap,itr*2)
                heapq.heappush(heap,itr*3)
                heapq.heappush(heap,itr*5)
                res.append(itr)
                s.add(itr)
        return res[n-1]