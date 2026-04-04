class Solution:
    def jump(self, nums: List[int]) -> int:
        count=0
        max_reach=[float('inf')]*(len(nums))
        max_reach[0] = 0
        i=0
        while i<len(nums):
            for itr in range(1,nums[i]+1):
                if i+itr>=len(nums):
                    break
                max_reach[i+itr] = min(max_reach[i+itr],max_reach[i]+1)
            i+=1
        print(max_reach)
        return max_reach[-1]    


            


        