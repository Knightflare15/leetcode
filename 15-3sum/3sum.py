class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = len(nums)-1
        while i > 1:
            l=0
            r=i-1
            while l<r:
                sumo = nums[l]+nums[r]+nums[i]
                if sumo>0:
                    r-=1
                    while r > -1 and nums[r]==nums[r+1]:
                        r-=1
                        
                elif sumo<0:
                    l+=1
                    while l < i and nums[l]==nums[l-1]:
                        l+=1
                    
                else:
                    ans.append([nums[l],nums[r],nums[i]])
                    l+=1
                    while l < i and nums[l]==nums[l-1]:
                        l+=1
                    r-=1
                    while r > -1 and nums[r]==nums[r+1]:
                        r-=1
            i-=1
            while i < len(nums)-1 and i>-1 and nums[i]==nums[i+1]:
                i-=1
        return ans

