class Solution:
    def canJump(self, nums: List[int]) -> bool:
       arr = [0] * len(nums)
       maxi = nums[0]
       for i in range(len(nums)):
        if i>maxi:
            break
        maxi = max(maxi,nums[i]+i)        

       return True if maxi >= len(nums)-1 else False