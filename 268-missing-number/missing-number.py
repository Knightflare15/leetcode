class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        sumo = l*(l+1)//2
        for i in nums:
            sumo-=i
        return sumo
        