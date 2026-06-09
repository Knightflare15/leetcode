class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = 0
        prefix = {}
        prefix[0] = 0
        vals = {0:1}
        for i,v in enumerate(nums):
            prefix[i+1] = prefix[i] + v
            if prefix[i+1]%k in vals:
                n+=vals[prefix[i+1]%k]
            vals[prefix[i+1]%k] = vals.get(prefix[i+1]%k,0)+1
        print(vals)
        print(prefix)
        return n