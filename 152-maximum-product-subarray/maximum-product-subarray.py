class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax = currmin = res = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                currmax,currmin = currmin,currmax
            currmax = max(currmax*nums[i],nums[i])
            currmin = min(currmin*nums[i],nums[i])
            res = max(currmax,res)
        return res
         

        
        