class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_reach = [nums[0]]
        i=1
        while i < (len(nums)):
            max_reached = max_reach[-1]
            if max_reached>=len(nums)-1:
                break
            while i <= max_reach[-1]:
                max_reached = max(max_reached,nums[i]+i)
                i+=1
            max_reach.append(max_reached)
        return len(max_reach)
            
            


        