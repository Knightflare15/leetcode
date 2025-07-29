import bisect
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 0
        tmp = k
        while True:
            tmp = k + prev
            i = bisect.bisect_right(arr,tmp)
            if i == prev:
                return k+i
            prev = i
        


        