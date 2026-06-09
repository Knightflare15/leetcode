class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_l = 0
        prefix = {0:0}
        vals = {0:0}
        for i,v in enumerate(nums):
            prefix[i+1] = prefix[i]+1 if v == 1 else prefix[i]-1
            if prefix[i+1]-0 in vals:
                l=vals[prefix[i+1]-0]
                max_l = max(i-l+1,max_l)
            vals[prefix[i+1]]=vals.get(prefix[i+1]-0,i+1)
        return max_l
        