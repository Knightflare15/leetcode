class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (r+l)//2
            if nums[l]>nums[mid]:
                r = mid
            elif nums[r]<nums[mid]:
                l = mid+1 if mid + 1 <len(nums) else mid
            elif nums[l]<=nums[r]:
                return nums[l]
        
        return nums[l]

        