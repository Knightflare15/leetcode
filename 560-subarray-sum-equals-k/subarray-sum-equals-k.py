class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = 0
        prefix = {}
        prefix[0]=0
        vals = {0:1}
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
            if prefix[i+1]-k in vals:
                n+=vals[prefix[i+1]-k]
            vals[prefix[i+1]] = vals.get(prefix[i+1],0)+1 
        return n