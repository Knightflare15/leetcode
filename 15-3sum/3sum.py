class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1
            sumo = 0
            while l < r:
                sumo=nums[i]+nums[l]+nums[r]
                if sumo == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif sumo > 0:
                    r-=1
                else :
                    l+=1
        rest = list(res)
        return rest

