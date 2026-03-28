class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        s = len(nums)
        def bt(arr,i):
            nonlocal result
            for itr in range(i+1,len(nums)):
                arr.append(nums[itr])
                result.append(arr[:])
                bt(arr,itr)
                arr.pop()
            return     
        bt([],-1)
        return result

