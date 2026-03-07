class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrL = [1 for i in nums]
        arrR = [1 for i in nums]
        l = len(nums) 
        for i in range(l):
            arrL[i] *= arrL[i-1]*nums[(i-1)] if i>0 else 1
            arrR[l-i-1] *= arrR[l-i]*nums[l-i] if i>0 else 1
        res = [1 for i in nums]
        for i in range(l):
            res[i] = arrL[i]*arrR[i]
        return res

        

            

        
