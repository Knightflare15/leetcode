class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        s = len(nums)
        def bt(arr,i):
            nonlocal result
            for itr in range(i+1,len(nums)):
                if itr > i+1 and nums[itr] == nums[itr-1]:
                    continue
                arr.append(nums[itr])
                result.append(arr[:])
                bt(arr,itr)
                arr.pop()
            return     
        bt([],-1)
        return result

