class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumo = nums[0]
        sumi = nums[0]
        for i in range(1,len(nums)):
            sumi = max(sumi+nums[i],nums[i])
            sumo = max(sumi,sumo)
        return sumo