class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = [1]*(len(nums)+1)
        currmax = nums[0]
        currmin = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                currmax,currmin = currmin,currmax
            currmax = max(currmax*nums[i],nums[i])
            currmin = min(currmin*nums[i],nums[i])
            res = max(res,currmax)
            

        
        return res
         

        
        