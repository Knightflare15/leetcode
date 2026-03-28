class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def bt(i,arr,visited):
            nonlocal res
            if len(visited) == len(nums):
                res.append(arr[:])
                return
            for itr in range(len(nums)):
                if itr == i or itr in visited:
                    continue
                arr.append(nums[itr])
                visited.add(itr)
                bt(itr,arr,visited)
                arr.pop()
                visited.discard(itr)
        bt(-1,[],visited)
        return res